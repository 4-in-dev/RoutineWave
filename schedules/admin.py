from django.contrib import admin

from .models import Category, Schedule

# Register your models here.
admin.site.register(Schedule)
admin.site.register(Category)