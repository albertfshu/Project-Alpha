from django import forms
from tasks.models import Task


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ("is_completed",)
