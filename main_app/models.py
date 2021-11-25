from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Memory(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  date = models.DateField('date of memory')
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("memories_detail", kwargs={"memory_id": self.id})
  