# Generated by Django 3.2.4 on 2021-06-09 01:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('research_site', '0002_rename_absract_publication_abstract'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=256, unique=True, verbose_name='Slug :'),
            preserve_default=False,
        ),
    ]
