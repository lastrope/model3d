__author__ = 'fgautier'

from django.db import models
from django.contrib.auth.models import User

class Models3d(models.Model):
    title = models.CharField(max_length=180)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User)
    publishing_date = models.DateField(auto_now_add=True)
    viewed_count = models.IntegerField(default=0) #Incremental value


