__author__ = 'fgautier'

from django.shortcuts import render
from model3d import models
"""
homepage
display main page with the list of all existing models3d
"""
def homepage(request):
    user = request.user
    mod3d = models.Models3d.objects.all().order_by('-id')
    return render(request, 'home.html', {'user': user, 'models3d': mod3d})
