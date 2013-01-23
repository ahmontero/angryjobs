# -*- encoding: utf-8 -*-

from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic.base import View

from recaptcha.client import captcha
#from twython import Twython

from web.forms import CommentForm
from web.models import Banner
from web.models import Comment
from web.models import Offer
from web.models import Tip


class OfferListView(ListView):
    model = Offer
    template_name = "web/main.html"
    context_object_name = "offers"
    paginate_by = 10

    def get_queryset(self):
        if self.request.method == 'GET':
            o = self.request.GET.get('o', None)
            if o:
                if 'company' in o:
                    o = o + '__name'
                    return Offer.objects.all().order_by(o)
                elif 'comments' in o:
                    if '-' in o:
                        return Offer.objects.all()\
                            .order_by('-number_of_comments')
                    else:
                        return Offer.objects.all()\
                            .order_by('number_of_comments')
                else:
                    return Offer.objects.all().order_by(o)
            else:
                return Offer.objects.all().order_by('-fetching_date')

    def get_context_data(self, **kwargs):
        context = super(OfferListView, self).get_context_data(**kwargs)

        context['banners'] = Banner.objects.all().order_by('fetching_date')
        context['first_row_tips'] = Tip.objects.filter(position=0)
        context['second_row_tips'] = Tip.objects.filter(position=1)
        context['third_row_tips'] = Tip.objects.filter(position=2)
        context['offers_number'] = Offer.objects.all().count()

        if self.request.method == 'GET':
            o = self.request.GET.get('o', None)
            if o:
                context['order'] = o

        #user = self.request.user

        #if user.is_authenticated():
        #    try:
        #        user_profile = user.get_profile()

        #        twitter = Twython(
        #        twitter_token=settings.CONSUMER_KEY,
        #        twitter_secret=settings.CONSUMER_SECRET,
        #        oauth_token=user_profile.twitter_profile\
        #            .oauth_profile.oauth_token,
        #        oauth_token_secret=user_profile.twitter_profile\
        #            .oauth_profile.oauth_secret)

        #        timeline = twitter.getHomeTimeline()
        #        context['twitter_user'] = user
        #        context['twitter_timeline'] = timeline
        #    except Exception:
        #        pass

        return context


class OfferDetail(View):
    context_object_name = "offer"
    template_name = 'web/offer_detail.html'

    def get_comments(self, offer):
        comments = Comment.objects.filter(offer=offer).order_by('-date')
        return comments

    def get(self, request, pk):
        offer = get_object_or_404(Offer, pk=pk)
        comments = self.get_comments(offer)
        form = CommentForm()

        return render_to_response(self.template_name, {'form': form,
            self.context_object_name: offer, 'comments': comments},
            context_instance=RequestContext(request))

    def post(self, request, pk):
        offer = get_object_or_404(Offer, pk=pk)
        request_params = dict([k, v] for k, v in request.POST.items())
        request_params.update({
                'user': request.user.id,
                self. context_object_name: offer.id
            })

        form = CommentForm(request_params)

        response = captcha.submit(
            request.POST.get('recaptcha_challenge_field'),
            request.POST.get('recaptcha_response_field'),
            settings.CAPTCHA_PRIVATE_KEY,
            request.META['REMOTE_ADDR'],)

        if not response.is_valid:
            captcha_response = 'ERROR'
            comments = self.get_comments(offer)
            return render_to_response(self.template_name, {'form': form,
                self.context_object_name: offer, 'comments': comments,
                'captcha_response': captcha_response},
                context_instance=RequestContext(request))

        if form.is_valid():
            form.save()
            offer.number_of_comments = offer.number_of_comments + 1
            offer.save()
            return redirect(reverse("web.offer.detail", args=(offer.id,)))
        else:
            comments = self.get_comments(offer)
            return render_to_response(self.template_name, {'form': form,
                self.context_object_name: offer, 'comments': comments},
                context_instance=RequestContext(request))


class LogoutView(RedirectView):
    def get_redirect_url(self, *kwargs):
        logout(self.request)
        url = reverse('web.index')
        return url

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)


class ErrorRedirect(RedirectView):
    """
        Redirect to index when raise errors ;-)
    """
    def get_redirect_url(self, *kwargs):
        return reverse('web.index')
