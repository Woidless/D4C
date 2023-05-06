from rest_framework import serializers
from django.db.models import Avg

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()


class ContractorSerializer(serializers.Serializer):

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        # print(instance, '\n'+'='*100)
        repr['rating'] = instance.reviews.aggregate(Avg('rating'))['rating__avg']
        return repr
    
    class Meta:
        model = models.Conractor
        exclude = ('id',)