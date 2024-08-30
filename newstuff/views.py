from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from logins_and_alerts.models import Drone, CUser, Alert
from django.contrib import messages
from django.contrib.auth.models import User

user_list = CUser.objects.all()  
drone_list = Drone.objects.all()
alerts_list = Alert.objects.all()
unread_alerts = 0
drone_active = 0
drone_not_active = 0
team_members = 0

def reloadlists():
    global user_list
    global drone_list
    global alerts_list
    user_list = CUser.objects.all()  
    drone_list = Drone.objects.all()
    alerts_list = Alert.objects.all()

def getdrones():
    reloadlists()
    global drone_active
    global drone_not_active
    drone_active = 0
    drone_not_active = 0
    for drone in drone_list:
        if drone.active:
            drone_active = drone_active + 1
        else:
            drone_not_active = drone_not_active + 1

def getunreadalerts():
    reloadlists()
    global unread_alerts
    unread_alerts = 0
    for alert in alerts_list:
        if not alert.is_read:
            unread_alerts = unread_alerts + 1

def getteam():
    reloadlists()
    global team_members
    team_members = 0
    for user in user_list:
        if user.is_in_team:
            team_members = team_members + 1

def dashboard(request):   
    getdrones()
    getunreadalerts()
    # User_instance = User.objects.create(user=current_user)
    return render(request, 'home.html', {'drone_active': drone_active, 'drone_not_active': drone_not_active, 'drone_list': drone_list, 'unread_alerts': unread_alerts, 'user_list': user_list, 'request': request})

def template(request):
    getunreadalerts()
    return render(request, "empty.html", {'unread_alerts': unread_alerts, 'user_list': user_list, 'request': request})


def drones(request):
    getdrones()
    getunreadalerts()
    return render(request, "drones.html", {'drone_list': drone_list, 'unread_alerts': unread_alerts, 'user_list': user_list, 'request': request})


def alerts(request): 
    getunreadalerts()
    return render(request, "alerts.html", {'unread_alerts': unread_alerts, 'user_list': user_list, 'request': request})

def reports(request): 
    getunreadalerts()
    return render(request, "reports.html", {'unread_alerts': unread_alerts, 'user_list': user_list, 'request': request})

def team(request): 
    getunreadalerts()
    return render(request, "team.html", {'unread_alerts': unread_alerts, 'user_list': user_list, 'request': request})

def settings(request):
    getunreadalerts()
    return render(request, "settings.html", {'unread_alerts': unread_alerts, 'user_list': user_list, 'request': request})       

def profile(request,username): 
    reloadlists()
    target = ''
    for user in user_list:
        if username == user.username:
            target = user
    return render(request, "profile.html", {'user_list': user_list, 'target': target})        


def maketeam(request, targetuser):
    reloadlists()
    for user in user_list:
        if targetuser == user.username:
            target = user
    target.is_in_team = True
    target.save()
    messages.success(request, (target.username + " has join the Team."))
    return redirect('homeapp:profile', username = target)

def makestaff(request, targetuser):
    reloadlists()
    for user in user_list:
        if targetuser == user.username:
            target = user
    target.is_staff = True
    target.save()
    messages.success(request, (target.username + " has join the Staff team."))
    return redirect('homeapp:profile', username = target)

def removeteam(request, targetuser):
    reloadlists()
    for user in user_list:
        if targetuser == user.username:
            target = user
    target.is_in_team = False
    target.save()
    messages.success(request, (target.username + " has been removed from the Team."))
    return redirect('homeapp:profile', username = target)

def removestaff(request, targetuser):
    reloadlists()
    for user in user_list:
        if targetuser == user.username:
            target = user
    target.is_staff = False
    target.save()
    messages.success(request, (target.username + " has been removed from the Staff team."))
    return redirect('homeapp:profile', username = target)
       