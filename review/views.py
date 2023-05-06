from django.shortcuts import render, get_object_or_404
from .models import Highway

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .permissions import IsAuthor
from . import serializers, models


def way_likes(request, way_id):
    way = get_object_or_404(Highway, pk=way_id)
    likes = way.likes.all()
    context = {'way': way, 'likes': likes}
    return render(request, 'way_likes.html', context)

class HighView(ModelViewSet):

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (permissions.IsAuthenticated(), IsAuthor())
        return (permissions.IsAuthenticatedOrReadOnly(),)

    