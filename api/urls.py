from django.urls import include, path
from rest_framework import routers

from achievement.views import AchievementViewSet, StatusViewSet, RankViewSet
from schedules.views import ScheduleViewSet
from scheduletemplates.views import SchedulestemplateViewSet


router = routers.DefaultRouter()
router.register(r'schedule', ScheduleViewSet)
router.register(r'achievement', AchievementViewSet)
router.register(r'status', StatusViewSet)
router.register(r'rank', RankViewSet)
router.register(r'Schedulestemplate', SchedulestemplateViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("", include("users.urls")),
]
