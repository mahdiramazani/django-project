# Generated by Django 4.2.3 on 2023-08-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0016_alter_newsmodels_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagegallery',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
