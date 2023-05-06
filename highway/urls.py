from django.urls import path
from .views import HighView

urlpatterns = [
    path('highway', HighView.as_view({'get':'list'})),
]
