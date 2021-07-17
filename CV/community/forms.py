from django import forms
from community.models import *


# Form (일반 폼)


class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['job', 'letter']
