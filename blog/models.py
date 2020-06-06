from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    info = models.TextField()
    picture = models.ImageField(upload_to='profile_pics')
    skills = ArrayField(models.CharField(max_length=80, blank=True))
