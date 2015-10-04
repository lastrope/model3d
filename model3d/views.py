__author__ = 'fgautier'

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from .forms import AddModelForm
from model3d.models import Models3d

from badges.signals import post_viewed, post_save_custom

"""
add_model3d
Provide a form to current user to add/post a new model3d
"""
def add_model3d(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = AddModelForm(request.POST)
            if form.is_valid():
                params = request.POST
                mod = Models3d(title=params['title'], description=params['description'], owner=request.user)
                mod._owner_id = mod.owner.id
                mod.save()
                post_save_custom.send(sender=None, mod=mod, owner=request.user) #see badges.models
                return HttpResponseRedirect('/')
        else:
            form = AddModelForm()
        return render(request, 'add_model3d.html', {'form': form})
    else:
        return HttpResponseRedirect('/users/login/')
"""
see_model3d
Detail of one selected by owner and model id a model3d and display
it in view
"""
def see_model3d(request, owner, model_id):
    owner= User.objects.get(username=owner)
    mod = Models3d.objects.get(owner_id=owner.id, id=model_id)
    if request.user != owner: # if current user see own post we don't count like a viewed time
        mod.viewed_count = mod.viewed_count + 1
        mod.save()
        post_viewed.send(sender=None, mod=mod, owner=owner)
    return render(request, 'see_model3d.html', {'mod': mod } )
"""
owner_model3d
Provides a list of current user model3d added yet
"""
def owner_model3d(request):
    if request.user.is_authenticated():
        mods = Models3d.objects.filter(owner_id=request.user.id)
        return render(request, 'owner_model3d.html', {'models3d': mods } )
    else:
        return HttpResponseRedirect('/users/login/')