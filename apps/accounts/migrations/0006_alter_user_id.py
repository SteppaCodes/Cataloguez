# Generated by Django 5.0.3 on 2024-03-06 21:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3667108a-1923-43c9-8931-0655acce259e'), primary_key=True, serialize=False, unique=True),
        ),
    ]
