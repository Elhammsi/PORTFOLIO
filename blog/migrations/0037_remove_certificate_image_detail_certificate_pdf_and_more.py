# Generated by Django 5.0.6 on 2024-06-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_certificate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='image_detail',
        ),
        migrations.AddField(
            model_name='certificate',
            name='pdf',
            field=models.FileField(default='pdfs/default.pdf', upload_to='pdfs/'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
