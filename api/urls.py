from django.urls import include, path
from rest_framework import routers

from schedules.views import ScheduleViewSet
from users.views import UserViewSet
from calendars.views import EventViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register(r'schedule', ScheduleViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("", include("users.urls")),
]
