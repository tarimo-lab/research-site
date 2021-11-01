# Generated by Django 3.2.4 on 2021-10-31 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_site', '0028_auto_20211031_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug(0ptional): post fix url for the post - no spaces'),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug(0ptional): post fix url for the project - no spaces'),
        ),
        migrations.AlterField(
            model_name='projectcategory',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug(0ptional): post fix url for the ProjectCategory - no spaces'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug(0ptional): post fix url for the publication - no spaces'),
        ),
    ]
