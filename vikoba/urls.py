from django.urls import path
from . import views

urlpatterns = [
    path('', views.deposit, name="deposit"),
    path('display/', views.display, name="display"),
]
