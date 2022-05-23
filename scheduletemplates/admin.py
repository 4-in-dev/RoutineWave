from django.contrib import admin

from .models import Scheduletemplate, Status

# Register your models here.
admin.site.register(Scheduletemplate)
admin.site.register(Status)