from django.contrib import admin

from .models import Category, Schedule, Status

# Register your models here.
admin.site.register(Schedule)
admin.site.register(Category)
admin.site.register(Status)