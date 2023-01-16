from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.Serializer) :
    class Meta :
        model = Account
        exclude = []