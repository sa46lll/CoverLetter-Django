from django.db import models


class CV(models.Model):
	job = models.CharField(max_length=50)
	letter = models.TextField()

	# def __str__(self):
	# 	return self.letter
