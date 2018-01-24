# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

ENVI_KEY_CONTEXT = "CONTEXT"
ENVI_KEY_SHOW_IN_ADMIN = "SHOW_IN_ADMIN"
ENVI_KEY_SHOW_IN_SITE = "SHOW_IN_SITE"

ENVI_ENVIRONMENT_LOCAL = "local"
ENVI_ENVIRONMENT_DEV = "dev"
ENVI_ENVIRONMENT_STAGE = "stage"
ENVI_ENVIRONMENT_PRODUCTION = "production"

ENVIRONMENTS = {
    ENVI_ENVIRONMENT_LOCAL: {
        ENVI_KEY_CONTEXT: {
            'CONTENT': "ENVIRONMENT: LOCAL",
            'COLOR_A': "#a0a0a0",
            'COLOR_B': "#7c7c7c",
        },
        ENVI_KEY_SHOW_IN_ADMIN: True,
        ENVI_KEY_SHOW_IN_SITE: True,
    },
    ENVI_ENVIRONMENT_DEV: {
        ENVI_KEY_CONTEXT: {
            'CONTENT': "ENVIRONMENT: DEVELOPMENT",
            'COLOR_A': "#2d88ff",
            'COLOR_B': "#1962c1",
        },
        ENVI_KEY_SHOW_IN_ADMIN: True,
        ENVI_KEY_SHOW_IN_SITE: True,
    },
    ENVI_ENVIRONMENT_STAGE: {
        ENVI_KEY_CONTEXT: {
            'CONTENT': "ENVIRONMENT: STAGING",
            'COLOR_A': "#ffba1e",
            'COLOR_B': "#dba11a",
        },
        ENVI_KEY_SHOW_IN_ADMIN: True,
        ENVI_KEY_SHOW_IN_SITE: True,
    },
    ENVI_ENVIRONMENT_PRODUCTION: {
        ENVI_KEY_CONTEXT: {
            'CONTENT': "ENVIRONMENT: PRODUCTION",
            'COLOR_A': "#ff1e1e",
            'COLOR_B': "#d61111",
        },
        ENVI_KEY_SHOW_IN_ADMIN: True,
        ENVI_KEY_SHOW_IN_SITE: False,
    }
}

ENVI_TEMPLATE_CONTEXT_ACCESSOR = "envi_context"
