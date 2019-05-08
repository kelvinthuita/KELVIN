from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length=40)
    occupation = models.CharField(max_length=40)
    slogan = models.CharField(max_length=40)
    residence = models.CharField(max_length=40)
    photo = models.ImageField()
    age = models.IntegerField()
    nationality = models.CharField(max_length=40)
    primary = models.CharField(max_length=40)
    secondary = models.CharField(max_length=40)
    email = models.EmailField()
    course = models.CharField(max_length=40)
    hobby = models.CharField(max_length=40)
    is_male = models.BooleanField(default=True)

    def _str_(self):
        return self.name
    def get_absolute_url(self):
        return reverse('afriqapp:index')



