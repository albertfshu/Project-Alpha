from django.contrib import admin
from projects.models import Project
from tasks.models import Task

# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
