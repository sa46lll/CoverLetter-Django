from django.forms import ModelForm
from community.models import *

class Form(ModelForm):
     class Meta:
         model = CV
         fields=['name', 'title', 'contents', 'url', 'email', 'fields']