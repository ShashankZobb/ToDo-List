from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=400)