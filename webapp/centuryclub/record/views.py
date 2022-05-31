from datetime import date, datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import RecordMonthTarget, RecordActivity

# Create your views here.
def index(request):
    user = User
    yearmonth = recordmonthlytarget(user)
    recordactivity = RecordActivity.objects.all()
    content = {
        'recordactivity': yearmonth
    }
    return render(request, "record.html", content)

def recordmonthlytarget(user):
    
    date = datetime.now()
    yearmonth = date.year + date.month
    return yearmonth

