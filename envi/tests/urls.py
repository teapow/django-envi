# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(
        regex=r'^admin/',
        view=admin.site.urls,
    ),
    url(
        regex=r'',
        view=TemplateView.as_view(template_name="envi/index.html"),
        name="index",
    ),
]
