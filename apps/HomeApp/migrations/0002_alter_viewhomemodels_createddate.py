# Generated by Django 4.2.3 on 2023-08-04 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewhomemodels',
            name='createdDate',
            field=models.DateTimeField(),
        ),
    ]
