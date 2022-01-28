from django import forms
from django.forms import ModelForm


from .models import *


class TaskForm(forms.ModelForm):            #Tablica Task i add edit delite
    # task = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'A new task...'}))

    class Meta:
        model = Task
        fields = '__all__'

