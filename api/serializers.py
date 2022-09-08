from rest_framework.serializers import ModelSerializer
from vikoba.models import Deposit


class DepositSerializer(ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'