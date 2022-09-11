from django.urls import path
from .views import DisplayView
from . import views

urlpatterns = [
    path('', DisplayView.as_view() , name="welcome"),
    path('deposit/', views.deposit, name="deposit"),
    path('display/', views.display, name="display"),
]
