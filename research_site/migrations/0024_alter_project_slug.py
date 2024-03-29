# Generated by Django 3.2.4 on 2021-10-31 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_site', '0023_alter_project_adviser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug(0ptional): name of the url for the project'),
        ),
    ]
