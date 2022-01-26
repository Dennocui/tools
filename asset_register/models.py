from pyexpat import model
from django.db import models

# Create your models here.

class Asset(models.Model):
    equipment =  models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    serial_number = models.CharField(max_length=100, null=True, blank=True)
    imei_one = models.CharField(max_length=50, null=True, blank=True) 
    imei_two = models.CharField(max_length=50, null=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    supplier = models.CharField(max_length=100, null=True, blank=True)
    purchase_price = models.IntegerField(max_length=50, null=True, blank=True)  
    device_name = models.CharField(max_length=50, null=True, blank=True)
    # current_user = models.CharField(max_length=50, null=True, blank=True)
    service_frequency = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField('Joined', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)


