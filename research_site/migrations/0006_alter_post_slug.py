# Generated by Django 3.2.4 on 2021-06-15 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_site', '0005_auto_20210614_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
