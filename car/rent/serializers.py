from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class BasicUserSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = BasicUser
        fields = '__all__'
        
class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Rent
        fields = '__all__'
        
class Carserailizer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'