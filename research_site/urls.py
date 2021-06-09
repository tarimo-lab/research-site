from django.urls import path

from .views import (HomePage, AboutPage, ProjectCategoryView, ProjectView, ProjectDetailView, PublicationView, PublicationDetailView, BlogView, BlogSingle)
from . import views

urlpatterns = [
	path('', HomePage.as_view(), name='home'),
	path('about/', AboutPage.as_view(), name='about'),
	path('categories/', ProjectCategoryView.as_view(), name='categories'),
	path('categories/<int:pk>/', views.categoryDetail, name='category_detail'),
	path('projects/', ProjectView.as_view(), name='projects'),
	path('projects/<str:slug>/', ProjectDetailView.as_view(), name='project_detail'),
	path('blogs/', BlogView.as_view(), name='blogs'),
	path('blogs/<str:slug>/', BlogSingle.as_view(), name='blog_detail'),
	path('publications/', PublicationView.as_view(), name='publications'),
	path('publications/<int:pk>/', PublicationDetailView.as_view(), name='publication_detail'),
]
