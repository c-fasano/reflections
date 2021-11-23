from django.db import models


from django.contrib.auth.models import User

# Create your models here.

class Memory(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  date = models.DateField('date of memory')
  user = models.ForeignKey(User, on_delete=models.CASCADE)