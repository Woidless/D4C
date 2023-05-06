from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from . import serializers, models


class ContractorView(ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    # serializer_class = serializers.
    queryset = models.Conractor.objects.all()

