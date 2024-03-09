# Generated by Django 5.0.3 on 2024-03-06 14:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('95da81cc-c571-4ba1-9f8e-c0748686e41b'), primary_key=True, serialize=False, unique=True),
        ),
    ]