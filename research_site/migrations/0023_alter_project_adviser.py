# Generated by Django 3.2.4 on 2021-10-31 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_site', '0022_auto_20211031_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='adviser',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
