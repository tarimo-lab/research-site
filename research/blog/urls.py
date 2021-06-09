from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.project_list, name='project-list'),
    path('project/<int:pk>', views.project_details, name='project-details'),
    path('blog', views.post_list, name='post-list'),
    path('post/<int:pk>', views.post_details, name='post-details'),
    path('post/<int:pk>/comment', views.comment, name='comment'),
    path('about', views.about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
