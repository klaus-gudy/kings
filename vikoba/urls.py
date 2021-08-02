from django.urls import path
from . import views

urlpatterns = [
    # path('', views.base, name="base"),
    path('', views.deposit, name="deposit"),
    path('display/', views.display, name="display"),
    path('login/', views.login, name="login"),
    path('welcome/', views.welcome, name="welcome"),
    path('logout/', views.logout, name="logout"),
]
