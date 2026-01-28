from django.db import models

class Speech(models.Model):
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    date = models.DateField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    picture = models.FileField(upload_to='speeches/', null=True, blank=True)
    add_later = models.BooleanField(default=False)
