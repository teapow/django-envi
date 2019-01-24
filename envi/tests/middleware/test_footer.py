# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.template.loader import render_to_string
from mock import MagicMock

from .base import BaseMiddlewareTestCase
from ... import constants
from ...middleware import EnviFooterMiddleware


class EnviFooterMiddlewareTestCase(BaseMiddlewareTestCase):
    """Test case for EnviFooterMiddleware."""

    middleware_class = EnviFooterMiddleware

    def test_update_response_modified_response_from_template_name(self):
        # update_response() should inject the rendered template if
        # head_html isn't provided in the call.
        markup = "<html><head></head></html>"
        response = MagicMock(content=markup)

        environment = {
            constants.ENVI_KEY_SHOW_IN_SITE: True,
            constants.ENVI_KEY_SHOW_IN_ADMIN: True,
            constants.ENVI_KEY_CONTEXT: {
                "CONTENT": "Test content goes here...",
                "COLOR_A": "#AAAAAA",
                "COLOR_B": "#CCCCCC",
            }
        }

        context = {"envi_context": environment[constants.ENVI_KEY_CONTEXT]}
        head_markup = render_to_string("envi/footer.html", context)

        middleware = self.middleware_class(environment=environment)
        updated_response = middleware.update_response(response)

        self.assertIn(head_markup, updated_response.content)
