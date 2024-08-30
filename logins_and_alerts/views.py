from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CUser, Drone
from .forms import CreateUserForm, UpdateUserForm, CreateDroneForm, UpdateDroneForm

def loginuser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homeapp:dashboard')
        else:
            messages.success(request, ("The username or the password are incorrect"))
            # return redirect('signin')
            return render(request, 'login.html' ,{})
    else:
        return render(request, 'login.html' ,{})
    
def logoutuser(request):
    logout(request)
    messages.success(request, ("You have logout"))
    return redirect('homeapp:dashboard')

def registeruser(request):
    form = CreateUserForm(request.POST or None, request.FILES)
    if form.is_valid():
        registered = form.save()
        User.objects.create_user(username=registered.username, password=registered.password, email = registered.email)
        #user = DefaultUser.objects.create_user(registered.username, registered.email, registered.password)
        user = authenticate(request, username=registered.username, password=registered.password)
        login(request, user)
        messages.success(request, ("Register Succesful!"))
        return redirect('homeapp:dashboard')
    else:
        messages.success(request, ("Register Failed!"))
        print(form.errors)
        form = CreateUserForm()
    return render(request, 'register.html' ,{"form":form})
    
def updateuser(request):
    user_list = CUser.objects.all() 
    for target in user_list:
        if target.username == request.user.username:
            user = target
    form = UpdateUserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, ("Profile Update Succesful!"))
        return redirect('homeapp:profile', username=user.username)
    return render(request, 'update.html' ,{"user":user, "form":form})

def registerdrone(request):
    form = CreateDroneForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, ("Drone Has Been Created!"))
        return redirect('homeapp:drones')
    else:
        #messages.success(request, ("Register Failed!"))
        print(form.errors)
        form = CreateDroneForm()
    return render(request, 'registerdrones.html' ,{"form":form})
    
def updatedrone(request, dronetarget):
    drone_list = Drone.objects.all() 
    for drone in drone_list:
        if dronetarget == drone.dronename:
            athing = drone
    form = UpdateDroneForm(request.POST or None, instance=athing)
    if form.is_valid():
        form.save()
        messages.success(request, ("Drone Update Succesful!"))
        return redirect('homeapp:drones')
    return render(request, 'updatedrones.html' ,{"drone":drone, "form":form})

def deletedrone(request, dronetarget):
    drone_list = Drone.objects.all() 
    for drone in drone_list:
        if dronetarget == drone.dronename:
            target = drone
    target.delete()
    messages.success(request, ("Drone Deleted Succesful!"))
    return redirect('homeapp:drones')
    #return render(request, 'updatedrones.html' ,{"drone":drone, "form":form})

#later to be deleted 
def testhtml(request):
    return render(request, 'testhtml.html')
