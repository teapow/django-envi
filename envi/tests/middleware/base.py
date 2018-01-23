# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from mock import Mock

from ..base import BaseTestCase


class BaseMiddlewareTestCase(BaseTestCase):
    """Base test class from which other Middleware tests should inherit."""

    def setUp(self):
        """Runs before each test."""
        self.request = Mock()
        self.response = Mock()
