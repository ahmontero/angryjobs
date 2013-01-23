# -*- encoding: utf-8 -*-


from tastypie.api import Api

from resources import (BannerResource, CompanyResource, OfferResource,
    ProfileResource, CommentResource)


v1 = Api(api_name="v1")
v1.register(ProfileResource())
v1.register(OfferResource())
v1.register(CompanyResource())
v1.register(BannerResource())
v1.register(CommentResource())
