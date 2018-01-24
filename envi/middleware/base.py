# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import resolve, Resolver404
from django.template.loader import render_to_string
from django.utils.encoding import force_unicode, force_bytes
from django.utils.translation import ugettext_lazy as _

from .. import constants
from ..conf import ENVIRONMENT

try:
    from django.utils.deprecation import MiddlewareMixin as _Base
except ImportError:
    _Base = object


class EnviBaseMiddleware(_Base):
    """Base middleware class for environments."""

    _required_keys = [
        constants.ENVI_KEY_SHOW_IN_SITE,
        constants.ENVI_KEY_SHOW_IN_ADMIN,
    ]

    def __init__(self, environment=None):
        """Attach the environment to self."""
        super(EnviBaseMiddleware, self).__init__()

        self.environment = environment or ENVIRONMENT
        self.validate_environment()

    def validate_environment(self):
        """Checks that the necessary keys are present in the environment."""
        for key in self._required_keys:
            if key not in self.environment.keys():
                message = _("Key: {k} not present in current environment")
                raise KeyError(message.format(k=key))

    def response_needs_updating(self, request, response):
        """Determines whether the environment should be shown."""
        # Check for response types where the banner can't be inserted.
        # Adapted from django_debug_toolbar.
        _encoding = response.get("Content-Encoding", "")
        _type = response.get("Content-Type", "").split(";")[0]

        is_ajax = request.is_ajax()
        is_streaming = getattr(response, "streaming", False)
        is_gzip = "gzip" in _encoding
        is_invalid = _type not in ("text/html", "application/xhtml+xml")

        if any([is_streaming, is_gzip, is_invalid, is_ajax]):
            return False

        try:
            is_admin = resolve(request.path).app_name == "admin"
        except Resolver404:
            return False

        # Check that the current environment is enabled for the request.
        show_in_admin = self.environment.get(constants.ENVI_KEY_SHOW_IN_ADMIN)
        show_in_site = self.environment.get(constants.ENVI_KEY_SHOW_IN_SITE)
        return (show_in_admin and is_admin) or (show_in_site and not is_admin)

    def update_response(self, response):
        """Abstract method. Needs to be implemented in subclasses."""
        raise NotImplementedError

    def process_response(self, request, response):
        """Injects the banner prior to the response being returned."""
        if self.response_needs_updating(request=request, response=response):
            response = self.update_response(response=response)

            if response.get("Content-Length"):
                response["Content-Length"] = len(response.content)

        return response


class EnviBaseTemplateMiddleware(EnviBaseMiddleware):
    """Extends the EnviBaseMiddleware to support templates."""
    template_name = None

    _required_keys = EnviBaseMiddleware._required_keys + [
        constants.ENVI_KEY_CONTEXT,
    ]

    def get_context_data(self):
        """Allows update of context data."""
        context = self.environment.get(constants.ENVI_KEY_CONTEXT, {})
        return {constants.ENVI_TEMPLATE_CONTEXT_ACCESSOR: context}

    def get_head_html(self, template_name=None):
        """Return a string to be injected in to the response <head> tag."""
        context = self.get_context_data()
        return render_to_string(template_name or self.template_name, context)

    def update_response(self, response, head_html=None):
        # Extract the HTML content from the response.
        html = force_unicode(response.content)
        if html.find("</head>") < 0:
            # No closing </head>, assuming it's a HTML snippet.
            return response

        if not head_html:
            head_html = self.get_head_html()

        # Insert the style rule just before the closing </head> tag.
        html = html.replace("</head>", head_html + "</head>", 1)

        # Finally, update the response.
        response.content = force_bytes(html)
        return response
