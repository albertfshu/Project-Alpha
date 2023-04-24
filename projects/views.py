from django.shortcuts import render
from projects.models import Project


# Create your views here.
def ProjectListView(request):
    projects = Project.objects.filter()
    context = {"projects": projects}
    return render(request, "projects/project_list.html", context)
