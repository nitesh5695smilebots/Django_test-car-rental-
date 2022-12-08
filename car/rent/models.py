from django.db import models
from django.contrib.auth.models import User

# Create your models here.

USER_TYPE= (('Customer','Customer'), ('Owner','Owner'))
GENDER_TYPE= (('Male','Male'), ('Female','Female'))

class BasicUser(models.Model):
	name = models.CharField(null=False, max_length=50)
	email = models.CharField(null=True, max_length=100,db_index=False,unique=False)
	phone = models.CharField(null=False, max_length=20,db_index=True,unique=True)
	secondaryPhone = models.CharField(null=True, max_length=20)
	passcode = models.CharField(null=False, max_length=20)
	gender = models.CharField(null=False, max_length=20, default='Male', choices=GENDER_TYPE)
	djangoUser = models.ForeignKey(User, null=False, related_name='django_user',on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	userType=models.CharField(null=False, max_length=100, default='Customer', choices=USER_TYPE)
	isActive = models.BooleanField(default=False)
	isEmailVerified=models.BooleanField(default=False)
	isPhoneVerified=models.BooleanField(default=False)  
	last_loggedIn=models.DateTimeField(auto_now=True)
	mobile_verify_OTP=models.CharField(null=True,blank=True,max_length=10)


	def __str__(self):
		return f"{str(self.name)} {str(self.phone)}"

Fuel_Type = (('Ev','Ev'),('Diesel','Diesel'),('Petrol','Petrol'),('CNG','CNG'),('LPG','LPG'))

class Car(models.Model):
    name = models.ForeignKey(BasicUser,on_delete=models.PROTECT)
    car_name = models.CharField(max_length=200,null=True)
    car_pic  =models.ImageField(upload_to='car_pic')
    fuel_type =models.CharField(max_length=6,choices=Fuel_Type)
    rent_price_hour = models.IntegerField(null=True)
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{str(self.name)} {str(self.car_name)} {str(self.fuel_type)},{str(self.is_available)},{str(self.is_active)}"

    
class Rent(models.Model):
    name = models.ForeignKey(BasicUser,on_delete=models.PROTECT)
    rent_car = models.ForeignKey(Car,on_delete=models.CASCADE)
    active_trip = models.DateTimeField(auto_now_add=True)
    end_trip = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
          return f"{str(self.name)} {str(self.active_trip)} {str(self.end_trip)}"
          

class HistoryRent(models.Model):
	owner_name = models.ForeignKey(Car,on_delete=models.PROTECT)
	rent_name = models.ForeignKey(Rent,on_delete=models.PROTECT)
	
	def __str__(self):
		return f"{str(self.owner_name.name),{str(self.rent_name.name)}}"
