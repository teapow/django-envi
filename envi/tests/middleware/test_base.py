# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from mock import MagicMock

from .base import BaseMiddlewareTestCase
from ... import constants
from ...conf import ENVIRONMENT
from ...middleware.base import EnviBaseMiddleware, EnviBaseTemplateMiddleware

KEY_ERROR_FORMAT = "Key: {k} not present in current environment"


class EnviBaseMiddlewareTestCase(BaseMiddlewareTestCase):
    """Tests for EnviBaseMiddleware."""

    middleware_class = EnviBaseMiddleware

    def test_init(self):
        # Tests that __init__ pulls the environment from settings.
        middleware = self.middleware_class()
        self.assertEqual(middleware.environment, ENVIRONMENT)

    def test_init_override(self):
        # Tests that you can override the environment through __init__.
        environment = {
            constants.ENVI_KEY_SHOW_IN_SITE: True,
            constants.ENVI_KEY_SHOW_IN_ADMIN: True,
            constants.ENVI_KEY_CONTEXT: {},
        }
        middleware = self.middleware_class(environment)
        self.assertEqual(middleware.environment, environment)

    def test_required_keys(self):
        # Tests that the required keys are present.
        environment = {
            constants.ENVI_KEY_SHOW_IN_SITE: True,
            constants.ENVI_KEY_SHOW_IN_ADMIN: True,
        }
        # Should not raise an exception when run.
        _ = self.middleware_class(environment)

    def test_required_keys_exception_a(self):
        # Tests that a KeyError is raised if a required key is not present.
        # constants.ENVI_KEY_SHOW_IN_ADMIN missing.
        environment = {constants.ENVI_KEY_SHOW_IN_SITE: True}
        with self.assertRaises(KeyError) as manager:
            _ = self.middleware_class(environment)

        self.assertEqual(
            KEY_ERROR_FORMAT.format(k=constants.ENVI_KEY_SHOW_IN_ADMIN),
            manager.exception.message,
        )

    def test_required_keys_exception_b(self):
        # Tests that a KeyError is raised if a required key is not present.
        # constants.ENVI_KEY_SHOW_IN_SITE missing.
        environment = {constants.ENVI_KEY_SHOW_IN_ADMIN: True}
        with self.assertRaises(KeyError) as manager:
            _ = self.middleware_class(environment)

        self.assertEqual(
            KEY_ERROR_FORMAT.format(k=constants.ENVI_KEY_SHOW_IN_SITE),
            manager.exception.message,
        )

    def test_update_response_called(self):
        # Test that update_response() is called if response_needs_updating
        # returns True.
        middleware = self.middleware_class()
        middleware.response_needs_updating = MagicMock(return_value=True)
        middleware.update_response = MagicMock()

        request = MagicMock()
        response = MagicMock()
        middleware.process_response(request, response)
        middleware.update_response.assert_called()

    def test_update_response_not_called(self):
        # Test that update_response() is not called if response_needs_updating
        # returns False.
        middleware = self.middleware_class()
        middleware.response_needs_updating = MagicMock(return_value=False)
        middleware.update_response = MagicMock()

        request = MagicMock()
        response = MagicMock()
        middleware.process_response(request, response)
        middleware.update_response.assert_not_called()

    def test_update_response_raises_exception(self):
        # Test that update_response() needs to be overridden in subclasses.
        middleware = self.middleware_class()
        middleware.response_needs_updating = MagicMock(return_value=True)

        request = MagicMock()
        response = MagicMock()

        with self.assertRaises(NotImplementedError):
            middleware.process_response(request, response)


class EnviBaseTemplateMiddlewareTestCase(BaseMiddlewareTestCase):
    """Tests for EnviBaseTemplateMiddleware."""

    middleware_class = EnviBaseTemplateMiddleware

    def test_required_keys(self):
        # Tests that the required keys are present.
        environment = {
            constants.ENVI_KEY_SHOW_IN_SITE: True,
            constants.ENVI_KEY_SHOW_IN_ADMIN: True,
            constants.ENVI_KEY_CONTEXT: {},
        }
        # Should not raise an exception when run.
        _ = self.middleware_class(environment)

    def test_required_keys_exception_a(self):
        # Tests that a KeyError is raised if a required key is not present.
        # contants.ENVI_KEY_CONTEXT missing.
        environment = {
            constants.ENVI_KEY_SHOW_IN_SITE: True,
            constants.ENVI_KEY_SHOW_IN_ADMIN: True,
        }
        with self.assertRaises(KeyError) as manager:
            _ = self.middleware_class(environment)

        self.assertEqual(
            KEY_ERROR_FORMAT.format(k=constants.ENVI_KEY_CONTEXT),
            manager.exception.message,
        )

    def test_required_keys_exception_b(self):
        # Tests that a KeyError is raised if a required key is not present.
        # contants.ENVI_KEY_SHOW_IN_ADMIN missing.
        environment = {
            constants.ENVI_KEY_SHOW_IN_SITE: True,
            constants.ENVI_KEY_CONTEXT: {},
        }
        with self.assertRaises(KeyError) as manager:
            _ = self.middleware_class(environment)

        self.assertEqual(
            KEY_ERROR_FORMAT.format(k=constants.ENVI_KEY_SHOW_IN_ADMIN),
            manager.exception.message,
        )

    def test_required_keys_exception_c(self):
        # Tests that a KeyError is raised if a required key is not present.
        # contants.ENVI_KEY_SHOW_IN_SITE missing.
        environment = {
            constants.ENVI_KEY_SHOW_IN_ADMIN: True,
            constants.ENVI_KEY_CONTEXT: {},
        }
        with self.assertRaises(KeyError) as manager:
            _ = self.middleware_class(environment)

        self.assertEqual(
            KEY_ERROR_FORMAT.format(k=constants.ENVI_KEY_SHOW_IN_SITE),
            manager.exception.message,
        )

    def test_get_context_data(self):
        # Tests that get_context_data() returns the value of the current
        # environment's constants.ENVI_KEY_CONTEXT.
        environment = {
            constants.ENVI_KEY_SHOW_IN_ADMIN: True,
            constants.ENVI_KEY_SHOW_IN_SITE: True,
            constants.ENVI_KEY_CONTEXT: {"hello": "world"},
        }

        middleware = self.middleware_class(environment)
        result = middleware.get_context_data()
        self.assertEqual(
            result[constants.ENVI_TEMPLATE_CONTEXT_ACCESSOR],
            {"hello": "world"},
        )

    def test_update_response_returns_unmodified_response(self):
        # If the response does not have a closing </head> tag, the original
        # response should be returned unmodified.
        markup = "<html></html>"
        response = MagicMock(content=markup)

        middleware = self.middleware_class()
        updated_response = middleware.update_response(response)

        self.assertEqual(response, updated_response)
        self.assertEqual(response.content, updated_response.content)

    def test_update_response_modifies_response_custom_head_html(self):
        # If the response does have a closing </head> tag, inject the
        # template in to the response content.
        markup = "<html><head></head></html>"
        head_html = "<test></test>"
        response = MagicMock(content=markup)

        middleware = self.middleware_class()
        middleware.get_head_html = MagicMock(return_value=head_html)

        updated_response = middleware.update_response(response)
        self.assertEqual(response, updated_response)
        self.assertEqual(len(response.content), len(markup) + len(head_html))
