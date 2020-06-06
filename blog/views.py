from django.shortcuts import render
from blog.models import Profile

def index(request):
    profiles = Profile.objects.all()
    return render(request, 'blog/index.html', {'profiles': profiles})
