# Generated by Django 3.0.7 on 2020-06-19 20:06

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
