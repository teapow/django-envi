# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import resolve, Resolver404
from django.template.loader import render_to_string
from django.utils.encoding import force_unicode, force_bytes

from .. import conf


class EnviBaseMiddleware(object):
    """ Base middleware class for environments. """

    def __init__(self):
        """ Attach the environment to self. """
        super(EnviBaseMiddleware, self).__init__()
        self.env = conf.ENVIRONMENT or {}

    def response_needs_updating(self, request, response):
        """ Determines whether the environment should be shown. """
        # Check for response types where the banner can't be inserted.
        # Adapted from django_debug_toolbar.
        _encoding = response.get('Content-Encoding', '')
        _type = response.get('Content-Type', '').split(';')[0]

        is_streaming = getattr(response, 'streaming', False)
        is_gzip = 'gzip' in _encoding
        is_invalid = _type not in ('text/html', 'application/xhtml+xml')

        if any([is_streaming, is_gzip, is_invalid]):
            return False

        try:
            is_admin = resolve(request.path).app_name == 'admin'
        except Resolver404:
            return False

        # Check that the current environment is enabled for the request.
        show_in_admin = self.env.get('SHOW_IN_ADMIN')
        show_in_site = self.env.get('SHOW_IN_SITE')
        return (show_in_admin and is_admin) or (show_in_site and not is_admin)

    def update_response(self, response):
        """ Abstract method. Needs to be implemented in subclasses. """
        raise NotImplemented

    def update_response_headers(self, response):
        """ Updates the response headers. """
        if response.get('Content-Length'):
            response['Content-Length'] = len(response.content)

    def process_response(self, request, response):
        """ Injects the banner prior to the response being returned. """
        if self.response_needs_updating(request=request, response=response):
            self.update_response(response=response)
            self.update_response_headers(response=response)

        return response


class EnviBaseTemplateMiddleware(EnviBaseMiddleware):
    """ Extends the EnviBaseMiddleware to support templates. """
    template_name = None

    def get_context_data(self, **kwargs):
        """ Allows update of context data. """
        context = self.env.get('CONTEXT', {})
        context.update(**kwargs)
        return context

    def update_response(self, response):
        # Extract the HTML content from the response.
        html = force_unicode(response.content)
        if html.find('</head>') < 0:
            # No closing </head>, assuming it's a HTML snippet.
            return response

        # Insert the style rule just before the closing </head> tag.
        head_html = render_to_string(
            template_name=self.template_name,
            context=self.get_context_data(),
        ) + '</head>'
        html = html.replace('</head>', head_html, 1)

        # Finally, update the response.
        response.content = force_bytes(html)
