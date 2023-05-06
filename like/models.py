from django.db import models

from django.contrib.auth import get_user_model

from highway.models import Highway

User = get_user_model()

class LikeCommentHighway(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    way = models.ForeignKey(Highway, on_delete=models.CASCADE, related_name='likes')
    created = models.DateTimeField(auto_now_add=True)
