# Generated by Django 4.2.1 on 2023-06-01 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0002_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='is_read',
        ),
    ]
