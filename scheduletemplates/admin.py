from django.contrib import admin

from .models import Category, Scheduletemplate, Status

# Register your models here.
admin.site.register(Scheduletemplate)
admin.site.register(Category)
admin.site.register(Status)