from django.urls import path

from . import views

app_name = 'loginsapp' 
urlpatterns = [
    path("signin/", views.loginuser, name="loginuser"),
    path("signout/", views.logoutuser, name="logoutuser"),
    path("register/", views.registeruser, name="registeruser"),
    path("update/", views.updateuser, name="updateuser"),
    path("adddrone/", views.registerdrone, name="adddrone"),
    path("updatedrone/<str:dronetarget>", views.updatedrone, name="updatedrone"),
    path("deletedrone/<str:dronetarget>", views.deletedrone, name="deletedrone"),
]