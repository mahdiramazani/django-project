# Generated by Django 4.2.3 on 2023-12-26 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcountApp', '0038_alter_otpclass_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpclass',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 20, 7, 1, 548844, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='passwordresettokenotp',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 20, 7, 1, 549844, tzinfo=datetime.timezone.utc)),
        ),
    ]
