from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from .views import (HomePage, AboutPage, ProfileCreateView, ProjectCategoryView, CategoryDetailView, ProjectCategoryCreateView, ProjectView, ProjectCreateView, ProjectDetailView, PublicationView, PublicationDetailView,PublicationCreateView, BlogView, BlogSingle, BlogCreateView)
from . import views

urlpatterns = [
	path('', HomePage.as_view(), name='home'),
	path('about/', AboutPage.as_view(), name='about'),
	path('create/profile/', ProfileCreateView.as_view(), name='profile_create'),
	path('categories/', ProjectCategoryView.as_view(), name='categories'),
	path('categories/<int:pk>/', views.categoryDetail, name='category_detail'),
	#path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
	path('projects/', ProjectView.as_view(), name='projects'),
	path('projects/<str:slug>/', ProjectDetailView.as_view(), name='project_detail'),
	path('create/project/', ProjectCreateView.as_view(), name='project_create'),
    path('create/project_category/', ProjectCategoryCreateView.as_view(), name='project_category_create'),
	path('blogs/', BlogView.as_view(), name='blogs'),
	path('blogs/<str:slug>/', BlogSingle.as_view(), name='blog_detail'),
	path('create/blog/', BlogCreateView.as_view(), name='blog_create'),
	path('publications/', PublicationView.as_view(), name='publications'),
	path('publications/<int:pk>/', PublicationDetailView.as_view(), name='publication_detail'),
	path('create/publication/', PublicationCreateView.as_view(), name='publication_create'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
