# Generated by Django 5.0.6 on 2024-05-21 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='title',
        ),
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
    ]
