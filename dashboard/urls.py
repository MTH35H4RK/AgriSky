from django.urls import path

from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("template/", views.template, name="template"),
    path("reports/", views.reports, name="reports"),
    path("alerts/", views.alerts, name="alerts"),
    path("drones/", views.drones, name="drones"),
]