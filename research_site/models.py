from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField 
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.urls import reverse_lazy
from django.utils.text import slugify



class Profile(models.Model):
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    headline = models.CharField(max_length=100, null=True)
    bio = models.TextField(max_length=350, null=True)
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
        
    def get_absolute_url(self):
        return reverse('about')


class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	content = RichTextField()
	created_date = models.DateTimeField(auto_now_add=True,verbose_name="Creation Date")
	post_image = models.FileField(upload_to='posts', blank = False,null = True,verbose_name="Add Photos to Article")
	slug = models.SlugField(unique=True, blank=True, null=True, verbose_name=_("Slug(0ptional): post fix url for the post - no spaces"))

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blogs')


	class Meta:
		ordering = ['-created_date']


class Publication(models.Model):
	title = models.CharField(max_length=400)
	author = models.CharField(max_length=400)
	publication_link = models.CharField(max_length=1000)
	abstract = RichTextField()
	created_date = models.DateTimeField(auto_now_add=False,verbose_name="Creation Date: YYYY-MM-DD")
	success_url = reverse_lazy('publications')
	slug = models.SlugField(unique=True, blank=True, null=True, verbose_name=_("Slug(0ptional): post fix url for the publication - no spaces"))
	
	def save(self, *args, **kwargs):
        	if not self.slug:
            		self.slug = slugify(self.title)
        	super(Publication, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('publications')
	class Meta:
		ordering = ('-created_date',)

        
class Gallery(models.Model):
	gallery_image = models.FileField(upload_to='gallery', blank = False,null = True,verbose_name="Add Photos to Gallery")
	
	def __str__(self):
		str_image = str(self.gallery_image)
		return str_image[8:-4]

class ProjectCategory(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    summary = RichTextField()
    # collaborators = models.CharField(max_length=300, null=True)
    proj_cat_image = models.FileField(upload_to='proj_cat_imageßs', blank = False,null = True,verbose_name="Add Photos to Project-Category")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name=_("Slug(0ptional): post fix url for the ProjectCategory - no spaces"))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ProjectCategory, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = _('Project Category')
        verbose_name_plural = _('Project Categories')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('categories')

    class Meta:
        ordering = ('-date',)

class Project(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    collaborators = models.CharField(max_length=300, null=True)
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Creation Date")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name=_("Slug(0ptional): post fix url for the project - no spaces"))
    project_image = models.FileField(upload_to='projects', blank = False,null = True,verbose_name="Add Photos to Project")
    adviser = models.CharField(max_length=300, blank=False, null=False)
    publish = models.BooleanField(
        verbose_name=_('Publish :'),
        default=True,
        help_text=_('Do you want to post this project?')
    )
    completed = models.BooleanField(
        verbose_name=_('Completed :'),
        default=False,
        help_text=_('is this project completed?')
    )
    category = models.ForeignKey('ProjectCategory', on_delete=models.CASCADE, verbose_name=_("Research Area"))
    content = RichTextField()


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('projects')

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
