# Generated by Django 4.2.3 on 2023-07-22 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0003_alter_newsmodels_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodels',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsmodels',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True),
        ),
    ]
