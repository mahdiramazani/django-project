# Generated by Django 4.2.3 on 2023-08-11 09:14

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('PaymentsApps', '0004_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordershop',
            name='pay_date',
            field=django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت'),
        ),
    ]
