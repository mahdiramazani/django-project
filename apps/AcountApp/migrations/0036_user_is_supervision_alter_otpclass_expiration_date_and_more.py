# Generated by Django 4.2.3 on 2023-09-30 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcountApp', '0035_alter_otpclass_expiration_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_supervision',
            field=models.BooleanField(default=False, verbose_name='عضو نظارت و بازرسی'),
        ),
        migrations.AlterField(
            model_name='otpclass',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 30, 17, 39, 7, 496867, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='passwordresettokenotp',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 30, 17, 39, 7, 496867, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='guild_member',
            field=models.BooleanField(default=False, verbose_name='عضو اتحادیه'),
        ),
    ]