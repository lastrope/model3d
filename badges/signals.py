__author__ = 'fgautier'

import django.dispatch

post_viewed = django.dispatch.Signal(providing_args=["mod", "owner"])
post_save_custom = django.dispatch.Signal(providing_args=["mod", "owner"])
post_login = django.dispatch.Signal(providing_args=["user"])