# Generated by Django 4.2.3 on 2023-07-22 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcountApp', '0005_user_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]