# Generated by Django 4.2.3 on 2023-07-24 07:08

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GuildRoomApp', '0004_guildroommodel_slug'),
        ('NewsApp', '0006_category_comment_newsmodels_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsmodels',
            options={'verbose_name': 'خبر', 'verbose_name_plural': 'اخبار'},
        ),
        migrations.AlterField(
            model_name='newsmodels',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='متن خبر'),
        ),
        migrations.AlterField(
            model_name='newsmodels',
            name='category',
            field=models.ManyToManyField(related_name='category', to='NewsApp.category', verbose_name='دسته بندی ها'),
        ),
        migrations.AlterField(
            model_name='newsmodels',
            name='image',
            field=models.FileField(upload_to='image/news', verbose_name='عکس خبر'),
        ),
        migrations.AlterField(
            model_name='newsmodels',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, verbose_name='اسلاگ:این قسمت پر نشود!'),
        ),
        migrations.AlterField(
            model_name='newsmodels',
            name='title',
            field=models.CharField(max_length=50, verbose_name='مقدمه'),
        ),
        migrations.AlterField(
            model_name='newsmodels',
            name='view',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='تعداد بازدید'),
        ),
        migrations.AlterField(
            model_name='newsmodels',
            name='writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='ادمین نویسنده'),
        ),
        migrations.AlterField(
            model_name='newsmodels',
            name='writer_guild',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GuildRoomApp.guildroommodel', verbose_name='اتحادیه نویسنده'),
        ),
    ]