# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from .base import EnviBaseTemplateMiddleware


class EnviFooterMiddleware(EnviBaseTemplateMiddleware):
    """ Renders a banner-style template in to the response. """
    template_name = "envi/footer.html"
