from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    headline = models.CharField(max_length=100, null=True)
    info = models.TextField(max_length=350, null=True)
    linkedin = models.CharField(max_length=250, null=True)
    github = models.CharField(max_length=250, null=True)
    facebook = models.CharField(max_length=250, null=True)
    instagram = models.CharField(max_length=250, null=True)
    twitter = models.CharField(max_length=250, null=True)
    picture = models.ImageField(upload_to='profile_pics', null=True)
    resume = models.FileField(upload_to ='docs', null=True)
    skills = models.CharField(max_length=300, null=True)

    @property
    def get_skills(self):
        return self.skills.split(',')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class UploadImages(models.Model):
    image =  models.ImageField(upload_to='files', null=True)

class UploadVedio(models.Model):
    vediofile = models.FileField(upload_to='files', null=True, verbose_name="")

class Project(models.Model):
    title = models.CharField(max_length=32, null=True)
    collaborators = models.ManyToManyField(Profile)
    abstract = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    html_content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class ResearchArea(models.Model):
    projects = models.ManyToManyField(Project)
    team = models.ManyToManyField(Profile)
    title = models.CharField(max_length=100, null=True)
    desription = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.title



class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=32, null=True)
    html_content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=30, null=True)
    body = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.body
