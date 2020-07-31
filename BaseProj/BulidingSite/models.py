from django.db import models

# Create your models here.

class addDev(models.Model):
    
    Name = models.CharField(max_length=20)
    Tool = models.CharField(max_length=20)
    Skills = models.CharField(max_length=1000)