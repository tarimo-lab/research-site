from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic, View
from django.db.models import Q
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Profile, Post, Publication, Project, ProjectCategory, Gallery

""" HomePage """
class HomePage(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = {
            'active_projects': Project.objects.order_by('-pk').filter(completed=False)[:5],
            'latest_categories': ProjectCategory.objects.order_by('-pk')[:10],
        }
        return render(request, self.template_name, context)

""" AboutPage """
class AboutPage(TemplateView):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        context = {
            'profiles': Profile.objects.order_by('-pk'),
        }
        return render(request, self.template_name, context)S