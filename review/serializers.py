from rest_framework import serializers
from django.db.models import Avg

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from like.models import LikeCommentHighway

from . import models

User = get_user_model()


class HighwaySerializer(serializers.Serializer):

    likes = LikeCommentHighway.objects.filter(way=id)

    class Meta:
        model = models.Highway
        exclude = ['id']