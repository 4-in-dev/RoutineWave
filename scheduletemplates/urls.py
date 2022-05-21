from django.urls import path

from .views import DetailCategory, ListCategory

urlpatterns = [
    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    path('status', ListCategory.as_view(), name='status'),
    path('status/<int:pk>/', DetailCategory.as_view(), name='singlestatus'),
]
