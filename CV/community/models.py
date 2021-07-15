from django.db import models

# Create your models here.
#class CV(models.Model):
#    contents = models.TextField()

class Post(models.Model):
    job=models.CharField(max_length=50)
    letter=models.TextField()
    #strength=models.CharField(max_length=50)

    def __str__(self):
        return self.letter
