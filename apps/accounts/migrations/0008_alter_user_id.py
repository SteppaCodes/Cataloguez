# Generated by Django 5.0.3 on 2024-03-14 13:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5a588010-f93a-4e9e-9f98-0f9d52756c42'), primary_key=True, serialize=False, unique=True),
        ),
    ]