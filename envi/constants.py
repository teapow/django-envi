# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

ENVIRONMENTS = {
    'local': {
        'CONTEXT': {
            'CONTENT': "ENVIRONMENT: LOCAL",
            'COLOR_A': "#a0a0a0",
            'COLOR_B': "#7c7c7c",
        },
        'SHOW_IN_ADMIN': True,
        'SHOW_IN_SITE': True,
    },
    'dev': {
        'CONTEXT': {
            'CONTENT': "ENVIRONMENT: DEVELOPMENT",
            'COLOR_A': "#2d88ff",
            'COLOR_B': "#1962c1",
        },
        'SHOW_IN_ADMIN': True,
        'SHOW_IN_SITE': True,
    },
    'stage': {
        'CONTEXT': {
            'CONTENT': "ENVIRONMENT: STAGING",
            'COLOR_A': "#ffba1e",
            'COLOR_B': "#dba11a",
        },
        'SHOW_IN_ADMIN': True,
        'SHOW_IN_SITE': True,
    },
    'production': {
        'CONTEXT': {
            'CONTENT': "ENVIRONMENT: PRODUCTION",
            'COLOR_A': "#ff1e1e",
            'COLOR_B': "#d61111",
        },
        'SHOW_IN_ADMIN': True,
        'SHOW_IN_SITE': False,
    }
}