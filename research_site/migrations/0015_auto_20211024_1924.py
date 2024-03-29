# Generated by Django 3.2.4 on 2021-10-24 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_site', '0014_auto_20211024_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='projectcategory',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation Date'),
        ),
    ]
