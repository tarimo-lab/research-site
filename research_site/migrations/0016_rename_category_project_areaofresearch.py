# Generated by Django 3.2.4 on 2021-10-26 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research_site', '0015_auto_20211024_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='category',
            new_name='areaOfResearch',
        ),
    ]