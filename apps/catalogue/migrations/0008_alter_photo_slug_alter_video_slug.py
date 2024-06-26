# Generated by Django 4.2.6 on 2024-03-31 17:43

import apps.catalogue.models
import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_photo_slug_video_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=False, null=True, populate_from=apps.catalogue.models._slugify_title_),
        ),
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=False, null=True, populate_from=apps.catalogue.models._slugify_title_),
        ),
    ]
