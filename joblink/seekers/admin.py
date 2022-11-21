from django.contrib import admin
from seekers.models import SeekerProfile,EducationInformation,ExpirenceInformation,SkillInformation

# Register your models here.
admin.site.register(SeekerProfile)
admin.site.register(EducationInformation)
admin.site.register(ExpirenceInformation)
admin.site.register(SkillInformation)

