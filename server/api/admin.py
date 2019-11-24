from django.contrib import admin
from .models import Ride, User, Driver

# Register your models here.
admin.site.register(Ride)
admin.site.register(User)
admin.site.register(Driver)
