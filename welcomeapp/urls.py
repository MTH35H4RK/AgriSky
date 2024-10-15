from django.urls import path

from . import views

app_name = 'welcomeapp' 
urlpatterns = [
    path("", views.welcomepage, name="welcomepage"),
]