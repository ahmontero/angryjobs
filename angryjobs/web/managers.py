# -*- encoding: utf-8 -*-


from django.db.models import Manager


class ProfileManager(Manager):
    def get_offers_for_profile(self, pk_profile=None):
        if pk_profile:
            return self.get_query_set().get(pk=pk_profile)
        else:
            return self.get_query_set().objects.all()
