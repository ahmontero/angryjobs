# -*- encoding: utf-8 -*-

from django.contrib import admin

from web.models import Banner
from web.models import Comment
from web.models import Company
from web.models import Offer
from web.models import Profile
from web.models import Tip
from web.models import TwitterProfile
from web.models import UserProfile


class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "fetching_date", "shitty"]
    list_filter = ["name", "fetching_date", "shitty"]
    readonly_fields = ("source",)


class OfferAdmin(admin.ModelAdmin):
    list_display = ["vacant", "company", "salary", "profile", "date",
        "fetching_date", "poblation", "premium"]
    list_filter = ["company", "profile", "salary", "poblation",
        "fetching_date", "premium"]
    readonly_fields = ("fetching_date", "source")


class BannerAdmin(admin.ModelAdmin):
    list_display = ["url", "fetching_date"]
    list_filter = ["url", "fetching_date"]


class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ["user"]
    list_filter = ["user"]

    readonly_fields = ("oauth_token", "oauth_secret")


class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "date", "offer", "text"]
    list_filter = ["user", "date", "offer", "text"]

admin.site.register(Company, CompanyAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.register(Profile)
admin.site.register(Tip)
admin.site.register(TwitterProfile)
admin.site.register(UserProfile)
