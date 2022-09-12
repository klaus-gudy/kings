from django.urls import path
from .views import DisplayView,DisplayDeposit,DepositView,IndividualDeposit
from . import views

urlpatterns = [
    path('', DisplayView.as_view() , name="welcome"),
    path('display/', DisplayDeposit.as_view() , name="display"),
    path('deposit/', DepositView.as_view() , name="deposit"),
    path('mydeposit/', IndividualDeposit.as_view() , name="mydeposit"),
]
