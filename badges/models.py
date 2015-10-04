__author__ = 'fgautier'

import datetime
import pytz

from django.db import models
from django.dispatch import receiver
from .signals import post_save_custom, post_viewed, post_login

from django.contrib.auth.models import User
from model3d.models import Models3d

class Badges(models.Model):
    title = models.CharField(max_length=180)
    description = models.CharField(max_length=255)
    owner = models.ManyToManyField(User, through='UserBadge') #prevent M2M issues

"""
UserBadge
Model used to make relation between User and Badges
(fix M2M eventuals issues)
"""
class UserBadge(models.Model):
    owner = models.ForeignKey(User)
    badge = models.ForeignKey(Badges)
    won_date = models.DateField(auto_now_add=True)

"""
 Helpers
"""
"""
 _helper_add_badge used to add a badge to user
"""
def _helper_add_badge(user, badge):
    ub = UserBadge.objects.create(owner=user, badge=badge)
    ub.save()
"""
_helper_had_badge test if a user had a badge yet
"""
def _helper_had_badge(user,badge):
    test = Badges.objects.filter(owner=user,title__exact=badge.title).count()
    if test > 0:
        return True
    else:
        return False
"""
Signals
"""
"""
Post save custom
Executed when user add a new model
"""
@receiver(post_save_custom)
def check_badge_add_model(sender, **kwargs):
    u = kwargs["owner"]
    count_model = Models3d.objects.filter(owner=u).count()
    if count_model == 1 :
        badge = Badges.objects.get(title='New Be')
        _helper_add_badge(u, badge)
    elif count_model == 5 :
        badge = Badges.objects.get(title='Pionner')
        _helper_add_badge(u, badge)
"""
Post viewed receiver
Executed when a Model has been viewed
"""
@receiver(post_viewed)
def check_badge_viewed(sender, **kwargs):
    badge = Badges.objects.get(title='Collector')
    if _helper_had_badge(kwargs['owner'], badge) == False:
        if kwargs['mod'].viewed_count == 1000: #1k viewed model
            _helper_add_badge(kwargs['owner'], badge)
"""
Post Login receiver
Executed after validation of auth process
"""
@receiver(post_login)
def check_inscription_date(sender, **kwargs):
    badge = Badges.objects.get(title='Star')
    if _helper_had_badge(kwargs['user'], badge) == False:
        now = datetime.datetime.now()
        oneyear = now - datetime.timedelta(days=365)
        testyear = (kwargs['user'].date_joined >= pytz.utc.localize(oneyear))
        if testyear:
            _helper_add_badge(kwargs['user'], badge)