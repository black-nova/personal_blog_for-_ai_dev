# Generated by Django 3.1.4 on 2020-12-17 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_task1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task1',
            old_name='completed',
            new_name='completed1',
        ),
        migrations.RenameField(
            model_name='task1',
            old_name='created',
            new_name='created1',
        ),
        migrations.RenameField(
            model_name='task1',
            old_name='title',
            new_name='title1',
        ),
    ]
