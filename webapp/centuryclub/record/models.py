from django.db import models

# Create your models here.
class RecordActivity(models.Model):
    pass
    # add additional fields in here
    username = models.CharField(null=True, blank=False, max_length=150)
    distance = models.IntegerField(blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name