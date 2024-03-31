# Generated by Django 4.2.6 on 2024-03-31 18:15

import apps.common.models
import autoslug.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=False, null=True, populate_from=apps.common.models._slugify_name_, unique=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]