from operator import mod
from django.db import models

# Create your models here.
class ApiTestModel(models.Model):
    title = models.CharField(max_length=255)