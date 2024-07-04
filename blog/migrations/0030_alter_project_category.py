# Generated by Django 5.0.6 on 2024-05-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_project_tools'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('ML', 'Machine Learning'), ('DL', 'Data Analysis'), ('Web', 'Web'), ('ALL', 'All')], max_length=100),
        ),
    ]
