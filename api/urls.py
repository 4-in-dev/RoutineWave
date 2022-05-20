from django.urls import include, path
from rest_framework import routers

from schedules.views import ScheduleViewSet

# from users.views import UserViewSet

router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)

router.register(r'schedule', ScheduleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('', include('dj_rest_auth.urls')),
    # path('', include('dj_rest_auth.registration.urls')),
    # path('', include('allauth.urls')),
    path("", include("users.urls")),
]
