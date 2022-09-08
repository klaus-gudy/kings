from django.urls import path

from .views import CreateDepositAPI,ListDepositAPI
urlpatterns = [
    path('create/', CreateDepositAPI.as_view(), name='depo_create'),
    path('list/', ListDepositAPI.as_view(), name='depo_list'),
]