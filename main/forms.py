from django import forms
from .models import job
from datetime import datetime
from django.forms import DateTimeInput

class JobForm(forms.ModelForm):
    class Meta:
        model = job

        fields = [
            "date",
            "work",
        ]
        widgets = {
            'date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }