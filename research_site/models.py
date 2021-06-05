from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import ugettext_lazy as _
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

class Gallery(models.Model):
	gallery_image = models.FileField(upload_to='gallery', blank = True,null = True,verbose_name="Add Photos to Gallery")

class ProjectCategory(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('Project Category')
        verbose_name_plural = _('Project Categories')

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        null=False,
        blank=False
    )
    collaborators = models.CharField(max_length=300, null=True)
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
    category = models.ManyToManyField(
        ProjectCategory
    )
    content = models.TextField()

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def display_category(self):
        return ', '.join([cat.title for cat in self.category.all()])

    def __str__(self):
        return self.title

    @property
    def get_collaborators(self):
        return self.collaborators.split(',')
