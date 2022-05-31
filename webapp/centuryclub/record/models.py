from django.db import models
import datetime

# Create your models here.
class RecordActivity(models.Model):
    pass
    # add additional fields in here
    username = models.CharField(null=True, blank=False, max_length=150)
    exercisetype = models.CharField(null=True, blank=False, max_length=50)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RecordMonthTarget(models.Model):
    username = models.CharField(null=True, blank=False, max_length=150)
    targetdistance = models.IntegerField(blank=True, null=True)
    targetdate = models.DateField(default=datetime.date.today)


class ExerciseType(models.Model):
    exercisetype = models.CharField(null=True, blank=False, max_length=50)
