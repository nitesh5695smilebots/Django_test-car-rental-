from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
# Create your views here.


class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = Carserailizer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class CarCreate(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = Carserailizer
    permission_classes = [IsAuthenticated]
    
class carEdit(generics.RetrieveUpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = Carserailizer
    permission_classes = [IsAuthenticated]

class RentHistory(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = Carserailizer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class Rent(generics.CreateAPIView):
    queryset =Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes = [IsAuthenticated]


    