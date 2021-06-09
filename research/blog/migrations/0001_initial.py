# Generated by Django 3.0.7 on 2020-08-11 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, null=True)),
                ('last_name', models.CharField(max_length=32, null=True)),
                ('info', models.TextField(null=True)),
                ('social', models.TextField(null=True)),
                ('picture', models.ImageField(null=True, upload_to='profile_pics')),
                ('skills', models.CharField(max_length=300, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, null=True)),
                ('abstract', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('html_content', models.TextField(blank=True, null=True)),
                ('collaborators', models.ManyToManyField(to='blog.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('desription', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('projects', models.ManyToManyField(to='blog.Project')),
                ('team', models.ManyToManyField(to='blog.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=32, null=True)),
                ('html_content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Profile')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30, null=True)),
                ('body', models.CharField(max_length=1000, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]
