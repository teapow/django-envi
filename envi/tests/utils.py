# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.http import HttpResponse
from mock import MagicMock


def make_mock_response():
    """Generate a mock object that behaves like a HttpResponse."""
    response = MagicMock(spec=HttpResponse)
    return response
