from django.contrib import admin
from .models import ExerciseType, RecordActivity, RecordMonthTarget


# Register your models here.
admin.site.register(RecordActivity)
admin.site.register(RecordMonthTarget)
admin.site.register(ExerciseType)

