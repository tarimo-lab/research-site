# Generated by Django 3.2.4 on 2021-08-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_site', '0010_projectcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='advisor',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
