from django.contrib import admin
from .models import CUser, Drone, Alert, Report


admin.site.register(CUser)
admin.site.register(Drone)
admin.site.register(Alert)
admin.site.register(Report)