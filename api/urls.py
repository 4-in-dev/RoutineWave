from django.urls import include, path
from rest_framework import routers

from achievement.views import TotalGraphViewSet
# from calendars.views import EventViewSet
from schedules.views import ScheduleViewSet
from scheduletemplates.views import SchedulestemplateViewSet

# from users.views import UserViewSet
# router.register(r'user', UserViewSet)

router = routers.DefaultRouter()
router.register(r'schedule', ScheduleViewSet)
# router.register(r'events', EventViewSet)
router.register(r'graph', TotalGraphViewSet)
router.register(r'Schedulestemplate', SchedulestemplateViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('', include('dj_rest_auth.urls')),
    # path('', include('dj_rest_auth.registration.urls')),
    # path('', include('allauth.urls')),
    path("", include("users.urls")),
]
