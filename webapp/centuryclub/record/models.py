from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
import datetime


class ExerciseType(models.Model):
    exercisetype = models.CharField(null=True, blank=False, max_length=50, help_text='Enter a core exercise type e.g. running')

    def __str__(self):
        return self.exercisetype #???


class RecordActivity(models.Model):
    pass
    # add additional fields in here
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    exercisetype = models.ForeignKey(ExerciseType, on_delete=models.SET_NULL, null=True, blank=False)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username #???


class RecordMonthTarget(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    targetdistance = models.IntegerField(blank=True, null=True)
    targetdate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.username #???
