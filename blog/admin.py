from django.contrib import admin

# Register your models here.
from .models import Project, Skill,Technology,Language,Images,text_about,experience,education,certificate


admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Technology)
admin.site.register(Language)
admin.site.register(Images)
admin.site.register(experience)
admin.site.register(education)
admin.site.register(text_about)
admin.site.register(certificate)