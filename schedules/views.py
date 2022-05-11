from rest_framework.decorators import api_view

from api import serializers

# Create your views here.


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            "Endpoint": "/notes/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of notes",
        },
        {
            "Endpoint": "/notes/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single note object",
        },
        {
            "Endpoint": "/notes/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates new note with data sent in post request",
        },
        {
            "Endpoint": "/notes/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Creates an existing note with data sent in post request",
        },
        {
            "Endpoint": "/notes/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting note",
        },
    ]
    return Response(routes)


# /notes GET
# /notes POST
# /notes/<id> GET
# /notes/<id> PUT
# /notes/<id> DELETE


import uuid

from rest_framework import generics, permissions, serializers, status, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.request import Request
from rest_framework.response import Response

from schedules.models import Schedule
from schedules.serializers import (ScheduleCreateSerializer,
                                   ScheduleSerializer,
                                   ScheduleUpdateSerializer)

from .models import Category
from .serializers import CategorySerializer, RegistrationSerializer


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",

                "User": serializer.data}, status=status.HTTP_201_CREATED
            )

        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


class ScheduleListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
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


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by('-id')
    serializer_class = ScheduleSerializer
