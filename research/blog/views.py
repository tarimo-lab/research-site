from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect, reverse
from blog.models import Profile, Project, Post, Comment, ResearchArea, UploadImages, UploadVedio
from blog.forms import CommentForm


def index(request):
    projects = Project.objects.all()[:2]
    research_areas = ResearchArea.objects.all()
    return render(request, 'blog/index.html', {'research_areas': research_areas,
                                                'projects': projects})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'blog/project_list.html', {'projects': projects})


def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'blog/project_details.html', {'project': project})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).all()
    return render(request, 'blog/post_details.html', {'post': post, 'comments': comments})


def comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('blog:post-details', args=[post.pk]))
        else:
            print(form.errors)
            return HttpResponse('Comment was unsuccessful.')


def about(request):
    profiles = Profile.objects.all()
    images = UploadImages.objects.all()
    vedios = UploadVedio.objects.all()
    return render(request, 'blog/about.html', {'profiles': profiles, 'images': images, 'vedios': vedios})
