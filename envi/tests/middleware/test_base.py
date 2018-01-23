# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from mock import MagicMock

from django.test.client import RequestFactory

from .base import BaseMiddlewareTestCase
from .. import utils
from ... import constants
from ...conf import ENVIRONMENT
from ...middleware.base import EnviBaseMiddleware


class EnviBaseMiddlewareTestCase(BaseMiddlewareTestCase):
    """Tests for EnviBaseMiddleware."""

    def test_init(self):
        # Tests that __init__ pulls the environment from settings.
        middleware = EnviBaseMiddleware()
        self.assertEqual(middleware.environment, ENVIRONMENT)

    def test_init_override(self):
        # Tests that you can override the environment through __init__.
        environment = {
            constants.ENVI_KEY_SHOW_IN_SITE: True,
            constants.ENVI_KEY_SHOW_IN_ADMIN: True,
            constants.ENVI_KEY_CONTEXT: {},
        }
        middleware = EnviBaseMiddleware(environment)
        self.assertEqual(middleware.environment, environment)

    def test_required_keys(self):
        # Tests that the required keys are present.
        environment = {
            constants.ENVI_KEY_SHOW_IN_SITE: True,
            constants.ENVI_KEY_SHOW_IN_ADMIN: True,
        }
        # Should not raise an exception when run.
        _ = EnviBaseMiddleware(environment)

    def test_required_keys_exception_a(self):
        # Tests that a KeyError is raised if a required key is not present.
        environment = {constants.ENVI_KEY_SHOW_IN_SITE: True}
        with self.assertRaises(KeyError):
            _ = EnviBaseMiddleware(environment)

    def test_required_keys_exception_b(self):
        # Tests that a KeyError is raised if a required key is not present.
        environment = {constants.ENVI_KEY_SHOW_IN_ADMIN: True}
        with self.assertRaises(KeyError):
            _ = EnviBaseMiddleware(environment)

    def test_update_response_called(self):
        # Test that update_response() is called if response_needs_updating
        # returns True.
        middleware = EnviBaseMiddleware()
        middleware.response_needs_updating = MagicMock(return_value=True)
        middleware.update_response = MagicMock()

        request = MagicMock()
        response = MagicMock()
        middleware.process_response(request, response)
        middleware.update_response.assert_called()

    def test_update_response_not_called(self):
        # Test that update_response() is not called if response_needs_updating
        # returns False.
        middleware = EnviBaseMiddleware()
        middleware.response_needs_updating = MagicMock(return_value=False)
        middleware.update_response = MagicMock()

        request = MagicMock()
        response = MagicMock()
        middleware.process_response(request, response)
        middleware.update_response.assert_not_called()

    # def test_response_needs_updating_admin_site(self):
    #     # Test that the response needs updating for an admin request when
    #     # ENVI_KEY_SHOW_IN_ADMIN is set to True.
    #     request_factory = RequestFactory()
    #     request = request_factory.get(
    #         path="admin:index",
    #         HTTP_X_REQUESTED_WITH="XMLHttpRequest",
    #     )
    #
    #     response = utils.make_mock_response()
    #
    #     environment = {
    #         constants.ENVI_KEY_SHOW_IN_SITE: True,
    #         constants.ENVI_KEY_SHOW_IN_ADMIN: True,
    #     }
    #
    #     middleware = EnviBaseMiddleware(environment)
    #     result = middleware.response_needs_updating(request, response)
    #     self.assertTrue(result)


class EnviBaseTemplateMiddlewareTestCase(BaseMiddlewareTestCase):
    """Tests for EnviBaseTemplateMiddleware."""
