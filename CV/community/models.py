from django.db import models

# Create your models here.
class CV(models.Model):
    contents = models.TextField()
