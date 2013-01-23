# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import *
from api import v1

urlpatterns = patterns('',
    (r'^api/', include(v1.urls)),
)
