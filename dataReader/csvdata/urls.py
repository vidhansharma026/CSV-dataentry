from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('insert/', views.insert_data),
    path('adddata/', views.adddata),
]