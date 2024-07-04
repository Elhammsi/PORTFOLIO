from django.db import models
from datetime import date
from django.utils.text import slugify
from django.urls import reverse
from django.core.exceptions import ValidationError

def validate_percentage(value):
    if value < 0 or value > 100:
        raise ValidationError('%(value)s is not a valid percentage', params={'value': value})
class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Machine-Learning', 'Machine-Learning'),
        ('Data-Analysis', 'Data-Analysis'),
        ('Web', 'Web'),
        ('ALL', 'All'),
    ]
    title = models.CharField(max_length=100, default="Default title")
    
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    date1 = models.DateField(default=date.today)
    date2 = models.DateField(default=date.today)
    description = models.TextField(default="Default description")
    image = models.ImageField(upload_to='images', null=True)
    tools = models.CharField(max_length=100, default="Default title")
  
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title

class Skill(models.Model):
    percentage = models.PositiveIntegerField(validators=[validate_percentage], default=50)
    skill = models.CharField(max_length=100, default="Default title")
    def __str__(self):
        return self.skill
class Language(models.Model):
     
    language = models.CharField(max_length=100, default="Default title")
    def __str__(self):
        return self.language
class Technology(models.Model):
     
    technology = models.CharField(max_length=100, default="Default title")
    def __str__(self):
        return self.technology
    
class Images(models.Model):
     
    image_detail =models.ImageField(upload_to='images')
    description = models.CharField(max_length=255, blank=True)
    def __str__(self):
          
        return self.description 
class text_about(models.Model):
    content1 = models.TextField()
    content2 = models.TextField()
    def __str__(self):
        return self.content1
class education(models.Model):
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=100, default="Default title")
    date=models.CharField(max_length=100)
    text = models.TextField()
    def __str__(self):
        return self.title
class experience(models.Model):
    title = models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    place = models.CharField(max_length=100, default="Default title")
    text = models.TextField()
    def __str__(self):
        return self.title
    
class certificate(models.Model):
    title = models.CharField(max_length=255,  blank=True)
    image_detail =models.ImageField(upload_to='images',default='images/default.jpg')
    def __str__(self):
        return self.title
    
 
       
