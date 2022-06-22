import imp
from django.contrib import admin
from .models import Job,CandidatesApplied
# Register your models here.

admin.site.register(Job)
admin.site.register(CandidatesApplied)