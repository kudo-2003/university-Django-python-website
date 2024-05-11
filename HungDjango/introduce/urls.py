from django.urls import path
from . import views

urlpatterns = [
    path('', views.introduce, name='introduce'),
]