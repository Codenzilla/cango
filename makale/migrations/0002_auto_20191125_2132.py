# Generated by Django 2.2.6 on 2019-11-25 18:32

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='makale',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Foto Ekle'),
        ),
        migrations.AlterField(
            model_name='makale',
            name='baslik',
            field=models.CharField(max_length=50, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='makale',
            name='içerik',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='makale',
            name='oluşturmaZamanı',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AlterField(
            model_name='makale',
            name='yazar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar'),
        ),
    ]
