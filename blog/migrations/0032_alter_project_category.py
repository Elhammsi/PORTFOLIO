# Generated by Django 5.0.6 on 2024-05-24 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_alter_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Machine-Learning', 'Machine Learning'), ('Data-Analysis', 'Data Analysis'), ('Web', 'Web'), ('ALL', 'All')], max_length=100),
        ),
    ]
