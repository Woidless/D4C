from django.shortcuts import render, get_object_or_404
from .models import Highway

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from . import serializers, models


class HighView(ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = serializers.HighwaySerializer
