# Generated by Django 4.2.3 on 2023-07-24 13:09

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0010_rename_cover_imagegallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodels',
            name='pub_date',
            field=django_jalali.db.models.jDateField(),
        ),
    ]
