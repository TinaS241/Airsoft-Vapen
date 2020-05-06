from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    location = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    team_page = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=4)


    

    def __str__(self):
        return self.username
    