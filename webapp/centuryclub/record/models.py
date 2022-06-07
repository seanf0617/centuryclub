from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
import datetime


# Create your models here.
class RecordActivity(models.Model):
    pass
    # add additional fields in here
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercisetype = models.CharField(null=True, blank=False, max_length=50)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.distance #???


class RecordMonthTarget(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    targetdistance = models.IntegerField(blank=True, null=True)
    targetdate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.objects #???


class ExerciseType(models.Model):
    exercisetype = models.CharField(null=True, blank=False, max_length=50)

    def __str__(self):
        return self.exercisetype #???
