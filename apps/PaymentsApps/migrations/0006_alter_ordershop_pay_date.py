# Generated by Django 4.2.3 on 2023-08-11 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaymentsApps', '0005_alter_ordershop_pay_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordershop',
            name='pay_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت'),
        ),
    ]
