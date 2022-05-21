from django.urls import include, path
from rest_framework import routers

from calendars.views import EventViewSet
from schedules.views import ScheduleViewSet

# from users.views import UserViewSet


router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)

router.register(r'schedule', ScheduleViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('', include('dj_rest_auth.urls')),
    # path('', include('dj_rest_auth.registration.urls')),
    # path('', include('allauth.urls')),
    path("", include("users.urls")),
]
