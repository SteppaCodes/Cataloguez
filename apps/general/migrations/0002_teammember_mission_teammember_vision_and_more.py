# Generated by Django 4.2.6 on 2024-03-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='mission',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='vision',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='desc',
            field=models.TextField(verbose_name='description'),
        ),
    ]
