from django.shortcuts import render, get_object_or_404
from .models import Project, Skill,Technology,Language,Images,education,experience,text_about,certificate

def starting_page(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    technology = Technology.objects.all()
    languages = Language.objects.all()
    educations = education.objects.all()
    experiences = experience.objects.all()
    text_abouts=text_about.objects.all()
    certificates=certificate.objects.all()
    return render(request, 'blog/index.html', {'projects': projects , 'skills': skills, 'technology': technology,'languages': languages ,'educations': educations,'experiences': experiences,'text_abouts':text_abouts,'certificates':certificates})

def portfolio_details(request, id):
    project= get_object_or_404(Project, id=id)
    images = Images.objects.all()
    return render(request, 'blog/details.html', {'project': project ,'images': images})

 

