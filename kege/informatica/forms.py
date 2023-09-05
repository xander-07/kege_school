from django import forms
from .models import Task, GeneratedTask

class GeneratedTaskForm(forms.ModelForm):
    tasks = forms.ModelMultipleChoiceField(queryset=Task.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = GeneratedTask
        fields = ('tasks',)