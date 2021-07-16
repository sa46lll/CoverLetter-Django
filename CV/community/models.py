from django.db import models
from django.urls import reverse


class Post(models.Model):

    job=models.CharField(max_length=50)
    letter = models.TextField()

    def __str__(self):
        return self.letter
