from django.db import models

# Create your models here.
class my_table(models.Model):
    name = models.CharField( max_length=50)
    age = models.IntegerField()