__author__ = 'fgautier'

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from badges.signals import post_login

from .forms import LoginForm
"""
logger
Using LoginForm class to display a login form and make active session
"""
def logger(request):
    if request.method == 'POST':
        # Form sent
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['login']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    post_login.send(sender=None, user=user) #see badges.models
                    return HttpResponseRedirect('/')
    else:
        #Form didn't sent
        user = None
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'user': user})
"""
logout_view
Simply used for logout current user
"""
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')