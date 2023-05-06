from django.urls import path, re_path

from . import views


urlpatterns = [
    path('liked/', views.toggle_like, name='like'),
]