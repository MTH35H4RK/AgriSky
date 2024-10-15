from django.shortcuts import render
from logins_and_alerts.models import Drone, CUser, Alert, Report

# Create your views here.
def welcomepage(request):
    return render(request, "welcomepage.html", {'request': request})
