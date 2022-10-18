from django.shortcuts import render
from rest_framework import serializers

from .models import Task
from .serializers import TaskSerializer
from rest_framework.viewsets import ModelViewSet


# Create your views here.

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
