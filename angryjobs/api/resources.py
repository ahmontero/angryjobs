# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django.conf.urls.defaults import url

from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.validation import Validation

from web.models import Offer, Company, Banner, Profile, Comment


"""
class EventResource(ModelResource):
    class Meta:
        resource_name = 'event'
        queryset = Event.objects.all()
        #allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        list_allowed_methods = ['get']

    def dehydrate(self, bundle):
        index = int(bundle.data['event_type'])
        bundle.data['event_name'] = Event.EVENT_TYPES[index][1]
        return bundle
"""

"""
class CustomApiKeyAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        username = request.META.get('HTTP_USERNAME')\
            or request.GET.get('username') or request.POST.get('username')
        api_key = request.META.get('HTTP_APIKEY')\
            or request.GET.get('api_key') or request.POST.get('api_key')

        if not username or not api_key:
            return self._unauthorized()
        try:
            user = User.objects.get(username=username)
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return self._unauthorized()
        request.user = user
        key = self.get_key(user, api_key)
        return key
"""


class ProfileResource(ModelResource):
    class Meta:
        queryset = Profile.objects.all()
        always_return_data = True
        resource_name = 'profile'
        fields = ['name', 'code', 'description']
        #detail_allowed_methods = ['get']
        list_allowed_methods = ['get']

        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class CompanyResource(ModelResource):
    class Meta:
        queryset = Company.objects.all().order_by('-fetching_date')
        always_return_data = True
        resource_name = 'company'
        #fields = ['link', 'source', 'name', 'shitty']
        #detail_allowed_methods = ['get', 'post', 'put', 'delete']
        list_allowed_methods = ['post', 'get']
        #validation = Validation()
        #filtering = {
        #    'author': ALL_WITH_RELATIONS,
        #    'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        #}

        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class OfferResource(ModelResource):
    company = fields.ForeignKey(CompanyResource, 'company', full=True)
    profile = fields.ForeignKey(ProfileResource, 'profile', full=True)

    class Meta:
        queryset = Offer.objects.all().order_by('-fetching_date')
        always_return_data = True
        resource_name = 'offer'
        #fields = ['username', 'first_name', 'last_name']
        #detail_allowed_methods = ['get']
        list_allowed_methods = ['post']

        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class BannerResource(ModelResource):

    class Meta:
        queryset = Banner.objects.all()
        always_return_data = True
        resource_name = 'banner'
        fields = ['url', 'fetching_date']
        #detail_allowed_methods = ['get', 'post', 'put', 'delete']
        list_allowed_methods = ['post']
        #validation = Validation()
        #filtering = {
        #    'author': ALL_WITH_RELATIONS,
        #    'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        #}

        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all().order_by('-date')
        always_return_data = True
        resource_name = 'comment'
        #fields = ['link', 'source', 'name', 'shitty']
        #detail_allowed_methods = ['get', 'post', 'put', 'delete']
        list_allowed_methods = ['get']
        #validation = Validation()

        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
