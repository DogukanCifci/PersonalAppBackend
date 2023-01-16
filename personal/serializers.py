from rest_framework import serializer
from .models import *

#Bütün modellerde sabit olacak seyleri FixSerializer'te yazicam

class FixSerializer(serializer.Model) :
    pass

###------------------ Serializers -----------------------

class DepartmentSerializer(FixSerializer) :
    class Meta : 
        model = Department
        exclude = []

class Personalserializer(FixSerializer) :
    class Meta :
        model = Personal
        exclude = []