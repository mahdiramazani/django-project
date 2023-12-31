# Generated by Django 4.2.3 on 2023-08-09 10:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EventsApp', '0003_remove_eventsmodel_user_of_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventsmodel',
            options={'verbose_name': 'رویداد', 'verbose_name_plural': 'رویداد ها'},
        ),
        migrations.AlterField(
            model_name='eventsmodel',
            name='users',
            field=models.ManyToManyField(related_name='event_user', to=settings.AUTH_USER_MODEL, verbose_name='کاربران رویداد'),
        ),
    ]
