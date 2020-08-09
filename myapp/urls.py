
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/time/', views.current_datetime, name='current_datetime'),
    path("<str:name>", views.name, name="name"),
]