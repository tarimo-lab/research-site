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
        return render(request, self.template_name, context)

""" Projects Category"""
class ProjectCategoryView(ListView):
    model = ProjectCategory
    template_name = 'categories.html'
    context_object_name = "categories"

def categoryDetail(request, pk):
    category = get_object_or_404(ProjectCategory, pk=pk)
    projects = Project.objects.filter(category=category).all()
    return render(request, 'category_detail.html', {'category': category, 'projects': projects})

class ProjectCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ProjectCategory
    template_name = 'create/new_project_category.html'
    fields = "__all__"
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
""" Projects """
class ProjectView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = "projects"

class ProjectDetailView(DetailView):
    model = Project
    template_name = "project_detail.html"


""" Publications """
class PublicationView(ListView):
    model = Publication
    template_name = 'publications.html'
    context_object_name = "publications"

class PublicationDetailView(DetailView):
    model = Publication
    template_name = "publication_detail.html"


""" Blog """

class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = "blogs"

class BlogSingle(generic.DetailView):
    model = Post
    template_name = 'blog_details.html'
    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs['slug'])

 
