from django.urls import path

from .views import DetailStatus, ListStatus

urlpatterns = [
    path('status', ListStatus.as_view(), name='status'),
    path('status/<int:pk>/', DetailStatus.as_view(), name='singlestatus'),
]
