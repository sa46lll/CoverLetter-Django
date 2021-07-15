from django.db import models

# Create your models here.
class CV(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)

    field_choices = (
        ("bp", "비판적사고"),
        ("bp1", "비판적사고"),
        ("bp2", "비판적사고"),
        ("bp3", "비판적사고"),
        ("bp4", "비판적사고"),
        ("bp5", "비판적사고"),
        ("bp6", "비판적사고"),
        ("bp7", "비판적사고"),
    )
    fields = models.CharField(max_length=8, choices=field_choices)
