from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from api import serializers

from .models import Note
from .serializers import NoteSerializer
from .utils import (createNote, deleteNote, getNoteDetail, getNotesList,
                    updateNote)


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


@api_view(["GET", "POST"])
def getNotes(request):
    if request.method == "GET":
        return getNotesList(request)

    if request.method == "POST":
        return createNote(request)


@api_view(["GET", "PUT", "DELETE"])
def getNote(request, pk):
    if request.method == "GET":
        return getNoteDetail(request, pk)

    if request.method == "PUT":
        return updateNote(request, pk)

    if request.method == "DELETE":
        return deleteNote(request, pk)


# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body=data['body']
#     )
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)


# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['DELETE'])
# def deleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()

#     return Response('Note was deleted!')

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.request import Request

from api.models import Schedule
from api.serializers import ScheduleSerializer, ScheduleCreateSerializer, ScheduleUpdateSerializer

from rest_framework import generics
from django.contrib.auth.models import User
from .models import Category
from .serializers import RegistrationSerializer, CategorySerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import serializers, status, permissions
import uuid

from rest_framework import viewsets


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


class ListUser(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by('-id')
    serializer_class = ScheduleSerializer
