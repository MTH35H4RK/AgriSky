from django.contrib import admin
from .models import CUser
from .models import Drone
from .models import Alert


admin.site.register(CUser)
admin.site.register(Drone)
admin.site.register(Alert)