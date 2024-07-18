# Generated by Django 4.2.14 on 2024-07-17 05:56

from django.db import migrations, models
import todoapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_todo_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=todoapp.models.upload_to),
        ),
    ]
