# Generated by Django 4.2.3 on 2023-08-13 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcountApp', '0031_alter_otpclass_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpclass',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 13, 15, 20, 22, 664781, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='passwordresettokenotp',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 13, 15, 20, 22, 665781, tzinfo=datetime.timezone.utc)),
        ),
    ]
