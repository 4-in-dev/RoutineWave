from django.urls import include, path
from rest_framework import routers

from schedules.views import ScheduleViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register(r'schedule', ScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
