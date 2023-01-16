from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import AccountSerializer
from .models import Account

class AccountView(ModelViewSet) :
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
