from datetime import datetime

from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Category, Scheduletemplate
from .serializers import (CategorySerializer, SchedulestemplateSerializer)


class SchedulestemplateViewSet(viewsets.ModelViewSet):
    queryset = Scheduletemplate.objects.all()
    serializer_class = SchedulestemplateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Scheduletemplate.objects.filter(writer=self.request.user)
        # print(self.request.query_params)
        if 'day' in self.request.query_params:
            print(f" day12 :{self.request.query_params}")
            queryset = queryset.filter(start_date=datetime.strptime(self.request.query_params['day'], '%Y-%m-%d'))
        elif 'month' in self.request.query_params:
            date1 = datetime.strptime(self.request.query_params['month'], '%Y-%m')
            date2 = datetime(date1.year, date1.month + 1, date1.day)
            queryset = queryset.filter(start_date__range=[date1, date2])
        return queryset
