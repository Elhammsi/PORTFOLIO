# Generated by Django 5.0.6 on 2024-05-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_rename_date_project_date1_project_date2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Machine Learning', 'Machine Learning'), ('Data Analysis', 'Data Analysis'), ('Web', 'Web'), ('ALL', 'All')], max_length=100),
        ),
    ]
