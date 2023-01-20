from django import forms
from . models import task

class form_task(forms.ModelForm):
    class Meta:
        model = task
        fields =['name','priority','date']