from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('', views.base, name="base"),
    path('', views.deposit, name="deposit"),
    path('display/', views.display, name="display"),
    # path('login/', views.login, name="login"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', views.register, name="register"),
    path('welcome/', views.welcome, name="welcome"),
    # path('logout/', views.logout, name="logout"),
    path('logout/', LogoutView.as_view(next_page='welcome'), name="logout"),
]
