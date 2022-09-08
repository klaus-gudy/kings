from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import DepositSerializer

from vikoba.models import Deposit

class CreateDepositAPI(CreateAPIView):
    serializer_class= DepositSerializer

class ListDepositAPI(ListAPIView):
    serializer_class= DepositSerializer
    model = Deposit
    queryset = Deposit.objects.all()