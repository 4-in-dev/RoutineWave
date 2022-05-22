from rest_framework import generics, permissions, serializers, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.request import Request
from rest_framework.response import Response

from api import serializers
from schedules.models import Schedule
from schedules.serializers import (ScheduleCreateSerializer,
                                   ScheduleSerializer,
                                   ScheduleUpdateSerializer)

from .models import Category
from .serializers import CategorySerializer

from rest_framework.permissions import IsAuthenticated
# Create your views here.
from datetime import datetime, time
from users.models import User
from rest_framework.views import APIView





# @api_view(["GET"])
# def getRoutes(request):
#     routes = [
#         {
#             "Endpoint": "/notes/",
#             "method": "GET",
#             "body": None,
#             "description": "Returns an array of notes",
#         },
#         {
#             "Endpoint": "/notes/id",
#             "method": "GET",
#             "body": None,
#             "description": "Returns a single note object",
#         },
#         {
#             "Endpoint": "/notes/create/",
#             "method": "POST",
#             "body": {"body": ""},
#             "description": "Creates new note with data sent in post request",
#         },
#         {
#             "Endpoint": "/notes/id/update/",
#             "method": "PUT",
#             "body": {"body": ""},
#             "description": "Creates an existing note with data sent in post request",
#         },
#         {
#             "Endpoint": "/notes/id/delete/",
#             "method": "DELETE",
#             "body": None,
#             "description": "Deletes and exiting note",
#         },
#     ]
#     return Response(routes)


# /notes GET
# /notes POST
# /notes/<id> GET
# /notes/<id> PUT
# /notes/<id> DELETE


#
# class RegistrationAPIView(generics.GenericAPIView):
#     serializer_class = RegistrationSerializer
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if (serializer.is_valid()):
#             serializer.save()
#             return Response({
#                 "RequestId": str(uuid.uuid4()),
#                 "Message": "User created successfully",
#
#                 "User": serializer.data}, status=status.HTTP_201_CREATED
#             )
#
#         return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


class ScheduleListView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Schedule.objects.order_by("-id")
    serializer_class = ScheduleSerializer

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ScheduleCreateView(CreateModelMixin, GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Schedule.objects.order_by("-id")
    serializer_class = ScheduleCreateSerializer

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ScheduleUpdateView(UpdateModelMixin, GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Schedule.objects.order_by("-id")
    serializer_class = ScheduleUpdateSerializer

    def update(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ListCategory(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class ScheduleViewSet(viewsets.ModelViewSet):
#     queryset = Schedule.objects.all().order_by('-id')
#     serializer_class = ScheduleSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        # print(self.request.data)
        serializer.save(writer=self.request.user,
                        end_date=self.request.data['end_date']
                              if 'end_date' in self.request.data else self.request.data['start_date'],
                        end_time=self.request.data['end_time'] if 'end_time' in self.request.data else time(23, 59)
                        )

    def get_queryset(self):
        queryset = Schedule.objects.filter(writer=self.request.user)
        # print(self.request.query_params)
        if 'day' in self.request.query_params:
            print(f" day12 :{self.request.query_params}")
            queryset = queryset.filter(start_date=datetime.strptime(self.request.query_params['day'], '%Y-%m-%d'))
        elif 'month' in self.request.query_params:
            date1 = datetime.strptime(self.request.query_params['month'], '%Y-%m')
            date2 = datetime(date1.year, date1.month + 1, date1.day)
            queryset = queryset.filter(start_date__range=[date1, date2])
        return queryset