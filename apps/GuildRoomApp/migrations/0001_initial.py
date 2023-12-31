# Generated by Django 4.2.3 on 2023-07-22 15:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildRoomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('post', models.CharField(blank=True, choices=[('ر', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=50, null=True)),
                ('user', models.ManyToManyField(limit_choices_to={'guild_member': True}, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
