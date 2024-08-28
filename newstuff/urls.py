from django.urls import path,include

from . import views

app_name = 'homeapp' 
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("template/", views.template, name="template"),
    path("alerts/", views.alerts, name="alerts"),
    path("reports/", views.reports, name="reports"),
    path("team/", views.team, name="team"),
    path("settings/", views.settings, name="settings"),
    path("drones/", views.drones, name="drones"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("maketeam/<str:targetuser>", views.maketeam, name="maketeam"),
    path("makestaff/<str:targetuser>", views.makestaff, name="makestaff"),
    path("removeteam/<str:targetuser>", views.removeteam, name="removeteam"),
    path("removestaff/<str:targetuser>", views.removestaff, name="removestaff"),
] 