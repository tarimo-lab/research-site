from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from . import models
# Register your models here.

admin.site.register(models.Post)
admin.site.register(models.Publication)
admin.site.register(models.Gallery)
admin.site.register(models.ProjectCategory)
admin.site.register(models.Project)
admin.site.register(models.Profile)