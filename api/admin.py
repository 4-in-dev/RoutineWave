from django.contrib import admin

from .models import Note

from .models import Schedule, Category
# Register your models here.


admin.site.register(Note)

admin.site.register(Schedule)
admin.site.register(Category)