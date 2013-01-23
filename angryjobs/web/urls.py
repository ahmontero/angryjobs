# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url

from web.views import LogoutView
from web.views import OfferDetail
from web.views import OfferListView


urlpatterns = patterns('',
    url(r'^$', OfferListView.as_view(), name="web.index"),
    url(r'^offers/(?P<pk>\d+)/$', OfferDetail.as_view(),
        name='web.offer.detail'),
    url(r'^logout/$', LogoutView.as_view(), name='web.logout'),

    #url(r'^twitter/$', DashboardView.as_view(), name='web.index'),
)
