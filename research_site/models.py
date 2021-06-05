from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    headline = models.CharField(max_length=100, null=True)
    bio = models.TextField(max_length=350, null=True)
    linkedin = models.CharField(max_length=250, null=True)
    github = models.CharField(max_length=250, null=True)
    picture = models.ImageField(upload_to='profile_pics', null=True)
    resume = models.FileField(upload_to ='docs', null=True)
    skills = models.CharField(max_length=300, null=True)

    @property
    def get_skills(self):
        return self.skills.split(',')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	content = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True,verbose_name="Creation Date")
	post_image = models.FileField(upload_to='posts', blank = True,null = True,verbose_name="Add Photos to Article")

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('Post', args=[str(self.id)])
	class Meta:
		ordering = ['-created_date']

class Publication(models.Model):
	title = models.CharField(max_length=400)
	author = models.CharField(max_length=400)
	pub_link = models.CharField(max_length=1000)
	absract = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True,verbose_name="Creation Date")
	
	def __str__(self):
		return self.title
	

class Gallery(models.Model):
	gallery_image = models.FileField(upload_to='gallery', blank = True,null = True,verbose_name="Add Photos to Gallery")
	
	def __str__(self):
		str_image = str(self.gallery_image)
		return str_image[8:-4]

class ProjectCategory(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()
    class Meta:
        verbose_name = _('Project Category')
        verbose_name_plural = _('Project Categories')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])

    class Meta:
        ordering = ('-date',)

class Project(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    collaborators = models.CharField(max_length=300, null=True)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Creation Date")
    slug = models.SlugField(
        max_length=256,
        verbose_name=_('Slug :'),
        unique=True,
        null=False,
        blank=False
    )
    project_image = models.FileField(upload_to='posts', blank = True,null = True,verbose_name="Add Photos to Article")
    publish = models.BooleanField(
        verbose_name=_('Publish :'),
        default=True,
        help_text=_('Will this post be published?')
    )
    completed = models.BooleanField(
        verbose_name=_('Completed :'),
        default=True,
        help_text=_('is this post completed?')
    )
    category = models.ForeignKey('ProjectCategory', on_delete=models.CASCADE)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.title

    @property
    def get_collaborators(self):
        return self.collaborators.split(',')

    class Meta:
        ordering = ('-created_date',)