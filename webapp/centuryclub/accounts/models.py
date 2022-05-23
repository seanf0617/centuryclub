from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    first_name= models.CharField(null=True, blank=False, max_length=100)
    last_name = models.CharField(null=True, blank=False, max_length=100)
    targetmiles = models.IntegerField(blank=True, null=True)
    location = models.CharField(null=True, blank=True, max_length=100)
    # DOB

    def __str__(self):
        return'{} {}'.format(self.first_name, self.last_name)
        