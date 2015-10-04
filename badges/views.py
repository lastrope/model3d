__author__ = 'fgautier'

from django.shortcuts import render
from badges.models import Badges
from django.http import HttpResponseRedirect

"""
mybadges
render : List of won badge about current logged user
"""
def mybadges(request):
    if request.user.is_authenticated():
        user = request.user
        mybadges = Badges.objects.filter(owner=request.user)
        return render(request, 'mybadges.html', {'user': user, 'badges' : mybadges, 'count' : mybadges.count()})
    else:
        return HttpResponseRedirect('/users/login/')