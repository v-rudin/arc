from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('show_records/', views.show_records),
]
