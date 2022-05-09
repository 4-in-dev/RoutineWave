from django.urls import path

from . import views

from django.urls import path, include
from .views import ListCategory, DetailCategory, ListUser, DetailUser, ScheduleListView
from rest_framework import routers
from .views import ScheduleViewSet

router = routers.DefaultRouter()
router.register(r'schedule', ScheduleViewSet)

urlpatterns = [
    # path("", views.getRoutes, name="routes"),
    path("notes/", views.getNotes, name="notes"),
    # path('notes/create/', views.createNote, name="create-note"),
    # path('notes/<str:pk>/update/', views.updateNote, name="update-note"),
    # path('notes/<str:pk>/delete/', views.deleteNote, name="delete-note"),
    path("notes/<str:pk>/", views.getNote, name="note"),

    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),

    path('users', ListUser.as_view(), name='users'),
    path('users/<int:pk>/', DetailUser.as_view(), name='singleuser'),

    path('', include(router.urls)), ]

