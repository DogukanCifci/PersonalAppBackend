from rest_framework import serializers
from .models import *

#Bütün modellerde sabit olacak seyleri FixSerializer'te yazicam

class FixSerializer(serializers.Serializer) :
    pass

###------------------ Serializers -----------------------

class DepartmentSerializer(FixSerializer) :
    class Meta : 
        model = Department
        exclude = []


class PersonalSerializer(FixSerializer) :
    class Meta :
        model = Personal
        exclude = []
