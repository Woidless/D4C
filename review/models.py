from django.db import models

from django.contrib.auth import get_user_model

from highway.models import Highway


User = get_user_model()


class Problem:
    problem = (
        ('Global', 'all street'),
        ('Local', 'piece of street'),
    )


class ReviewHighway(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    way = models.ForeignKey(Highway, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    image = models.ImageField()
    rating = models.IntegerField()
    problem = models.CharField(choices=Problem.problem)
    created = models.DateTimeField(auto_now_add=True)

    def __sts__(self):
        return self.user
