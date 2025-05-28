from django import forms
from .models import Job, Application  # ✅ Make sure Application is imported

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['job', 'applicant_email', 'resume']  # This line is causing the issue





