# Generated by Django 3.2.4 on 2021-06-26 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_site', '0009_auto_20210615_0430'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcategory',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]