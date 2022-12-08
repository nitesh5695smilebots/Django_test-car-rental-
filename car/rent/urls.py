from .models import *
from django.urls import path
from . import views


urlpatterns = [
    path('carList/',views.CarList.as_view(),name='car_list'),
    path('carEdit/<int:pk>/',views.carEdit.as_view(),name='car_edit'),
    path('rent_history/',views.RentHistory.as_view(),name='rent_history'),
    path('create_rent/',views.Rent.as_view(),name='car_rent'),
    path('car_create/',views.CarCreate.as_view(),name='car_create'),
    

]
