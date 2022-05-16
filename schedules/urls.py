from django.urls import include, path
from rest_framework import routers

from .views import (DetailCategory, ListCategory, ScheduleListView,)



urlpatterns = [
    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    path('schedules', ScheduleListView.as_view(), name='schedules'),
]
