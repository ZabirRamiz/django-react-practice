from django.db import models

# Create your models here.
class something(models.Model):
    someone = models.CharField( max_length=50)
    noone = models.CharField( max_length=50)

class who(models.Model):
    name = models.CharField( max_length=50)
    tell = models.CharField( max_length=50)