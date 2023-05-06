from django.db import models
from contractor.models import Conractor

# from review.models import ReviewHighway


class Status:
    status = (
        ('red', 'worse way'),
        ('yellow', 'in profress'),
        ('green', 'satisfactorily'),        
    )


class Highway(models.Model):
    title = models.CharField(max_length=50)
    material = models.CharField(max_length=100)
    contractor = models.ForeignKey(Conractor, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(choices=Status.status)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lifetime = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    expiration_date = models.DateTimeField(null=True,blank=True)

    def __sts__(self):
        return self.title