# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf import settings

from . import constants

ENVIRONMENT_KEY = getattr(
    settings,
    'ENVI_ENVIRONMENT_KEY',
    'local'
)

ENVIRONMENTS = getattr(
    settings,
    'ENVI_ENVIRONMENTS',
    constants.ENVIRONMENTS
)

ENVIRONMENT = getattr(
    settings,
    'ENVI_ENVIRONMENT',
    constants.ENVIRONMENTS[ENVIRONMENT_KEY]
)
