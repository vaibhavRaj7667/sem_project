# Generated by Django 5.1 on 2024-08-14 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='questions',
            new_name='question',
        ),
    ]
