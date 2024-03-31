# Generated by Django 4.2.6 on 2024-03-31 18:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3b590506-f87a-4f0d-af1f-b958c024c029'), primary_key=True, serialize=False, unique=True),
        ),
    ]