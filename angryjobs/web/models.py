# -*- encoding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from twitter import signals
from twitter.models import OAuthProfile

from managers import ProfileManager


class TwitterProfile(models.Model):
    oauth_profile = models.OneToOneField(OAuthProfile)
    img = models.CharField(max_length=1024, blank=True, null=True)
    screen_name = models.CharField(max_length=1024, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.oauth_profile


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    twitter_profile = models.OneToOneField(TwitterProfile)

    def __unicode__(self):
        return u'%s from %s' % (self.twitter_profile, self.user)


class Tip(models.Model):

    PRIORITIES = (
        (0, _(u'Baja')),
        (1, _(u'Media')),
        (2, _(u'Alta')),
    )

    POSITIONS = (
        (0, _(u'1ª Fila')),
        (1, _(u'2ª Fila')),
        (2, _(u'3ª Fila')),
    )

    header = models.CharField(max_length=512)
    header_tooltip = models.CharField(max_length=1024, blank=True, null=True)
    body = models.TextField(max_length=1024)
    body_tooltip = models.CharField(max_length=1024, blank=True, null=True)
    priority = models.IntegerField(choices=PRIORITIES)
    position = models.IntegerField(choices=POSITIONS)

    icon_name = models.CharField(max_length=512)

    def __unicode__(self):
        return u'%s (%s)' % (self.id, self.header)


class Profile(models.Model):
    name = models.CharField(max_length=256)
    code = models.IntegerField(unique=True)
    description = models.CharField(max_length=1024)
    objects = ProfileManager()

    def __unicode__(self):
        return u'%s (code: %s)' % (self.name, self.code)


class Banner(models.Model):
    fetching_date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=320, unique=True)

    def __unicode__(self):
        return u'%s' % (self.url)


class Company(models.Model):
    fetching_date = models.DateTimeField(auto_now_add=True)
    link = models.URLField()

    cid = models.CharField(max_length=256, unique=True)
    source = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    shitty = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % (self.name)


class Offer(models.Model):
    company = models.ForeignKey(Company)
    profile = models.ForeignKey(Profile, blank=True, null=True)

    fetching_date = models.DateTimeField(auto_now_add=True)
    link = models.URLField()

    source = models.CharField(max_length=256)

    vacant = models.CharField(max_length=256, unique=True)
    poblation = models.CharField(max_length=256)
    date = models.CharField(max_length=256)

    description = models.CharField(max_length=5000, blank=True, null=True)
    premium = models.BooleanField(default=False)
    css_class = models.CharField(max_length=256)

    level = models.CharField(max_length=5000, blank=True, null=True)
    description = models.TextField(max_length=1024)
    min_form = models.CharField(max_length=5000, blank=True, null=True)
    min_exp = models.CharField(max_length=5000, blank=True, null=True)
    min_req = models.CharField(max_length=5000, blank=True, null=True)
    des_req = models.CharField(max_length=5000, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    number_of_vacants = models.IntegerField(blank=True, null=True)

    number_of_comments = models.IntegerField(default=0, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.vacant)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments')
    offer = models.ForeignKey(Offer, related_name='offer')
    text = models.TextField(max_length=5000, blank=False, null=False)

    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s on %s' % (self.user, self.offer)


def tokens_received(sender, request, screen_name, oauth_token,
    oauth_token_secret, **kwargs):

    def log_user_in(request, user=None):
        user = authenticate(username=user.username,
            password=settings.GLOBAL_PWD)
        if user:
            login(request, user)
    try:
        user = User.objects.get(username__iexact=screen_name)
        if user:
            log_user_in(request, user)
    except User.DoesNotExist:
        user = User.objects.create_user(username=screen_name,
            email="twitter@auto-created.com", password=settings.GLOBAL_PWD)
        user.save()

        oauth_profile = OAuthProfile(oauth_token=oauth_token,
            oauth_secret=oauth_token_secret)
        oauth_profile.save()

        twitter_profile = TwitterProfile(oauth_profile=oauth_profile,
            screen_name=screen_name)
        twitter_profile.save()

        user_profile = UserProfile(user=user,
            twitter_profile=twitter_profile)
        user_profile.save()

        log_user_in(request, user)


signals.tokens_received.connect(tokens_received)
