# Generated by Django 4.2.3 on 2023-09-30 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0006_alter_viewhomemodels_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewhomemodels',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
