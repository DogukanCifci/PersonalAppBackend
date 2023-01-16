from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

#Bütün modellerde sabit olacak #created_date , 'updated_date' vb.... FixSerializer'te yazicam

class FixView(ModelViewSet) :
    pass

###------------------ Views -----------------------

class DepartmentView(FixView) :
    queryset = Department.objects.all()
    print(queryset)
    serializer_class = DepartmentSerializer

class PersonalView(FixView) :
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

