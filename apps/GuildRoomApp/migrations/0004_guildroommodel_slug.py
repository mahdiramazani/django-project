# Generated by Django 4.2.3 on 2023-07-24 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuildRoomApp', '0003_alter_guildroommodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='guildroommodel',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True),
        ),
    ]
