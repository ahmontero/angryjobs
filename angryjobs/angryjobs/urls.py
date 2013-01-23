# -*- encoding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from web.views import ErrorRedirect


urlpatterns = patterns('',
    url(r'^', include('web.urls')),
    url(r'^', include('api.urls')),
    url(r'^twitter/', include('twitter.urls')),
)

if settings.DEBUG:
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns += patterns('',
        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
    )
else:
    #from django.conf.urls.defaults import *
    #from django.conf.urls.defaults import handler301
    #from django.conf.urls.defaults import handler302
    from django.conf.urls.defaults import handler404
    from django.conf.urls.defaults import handler500

    handler404 = ErrorRedirect.as_view()
    handler500 = ErrorRedirect.as_view()
    #handler301 = ErrorRedirect.as_view()
    #handler302 = ErrorRedirect.as_view()

urlpatterns += staticfiles_urlpatterns()

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    )

