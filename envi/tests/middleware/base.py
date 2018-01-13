# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from mock import Mock

from ..base import BaseMiddlewareTestCase
from ...middleware import EnviFooterMiddleware


class EnviBaseTemplateMiddleware(BaseMiddlewareTestCase):
    """Base test class from which other Middleware tests should inherit."""

    def setUp(self):
        """Runs before each test."""
        self.middleware = EnviFooterMiddleware()
        self.request = Mock()
        self.response = Mock()
