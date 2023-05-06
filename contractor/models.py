from django.db import models


class Conractor(models.Model):
    image = models.ImageField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)

    def __sts__(self):
        return self.email