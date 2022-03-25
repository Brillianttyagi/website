from os.path import join
from uuid import uuid4

from account.models import Account
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid4(), ext)
    return join('inventory/', filename)

class Inventory(models.Model):
    #product regard field
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    name= models.CharField(max_length=200,blank=True,null=True)
    description = models.CharField(max_length=1000,blank=True,null=True)
    image = models.ImageField(upload_to=get_file_path)
    category = models.CharField(max_length=100,blank=True,null=True)
    subCategory = models.CharField(max_length=100,blank=True,null=True)
    HSN = models.CharField(max_length=100,blank=True,null=True)
    warranty = models.CharField(max_length=100,blank=True,null=True)
    guarantee = models.CharField(max_length=100,blank=True,null=True)
    length = models.CharField(max_length=100,blank=True,null=True)
    width = models.CharField(max_length=100,blank=True,null=True)
    height = models.CharField(max_length=100,blank=True,null=True)
    weight = models.FloatField(default=0)
    marked = models.CharField(max_length=100,blank=True,null=True)
    colors = models.CharField(max_length=100,default='',null=True,blank=True)
    material = models.CharField(max_length=100,blank=True,null=True)
    date = models.DateTimeField(default=timezone.now)
    countryOfOrigin = models.CharField(max_length=100,blank=True,null=True)

  
    
    #city = models.CharField(max_length=100,blank=True,null=True)
    inventoryStatus = models.BooleanField(default=True)
    shippingWithSeventhSquare = models.BooleanField(default=True)
    #inventory regard field
    qty = models.FloatField(validators=[MinValueValidator(0)],default=0.0)
    markedPrice = models.FloatField(validators=[MinValueValidator(0)])
    sellingPrice = models.FloatField(validators=[MinValueValidator(0)],blank=True,null=True)
    commercialPrice = models.FloatField(validators=[MinValueValidator(0)], default=0.0, blank=True,null=True)

    aboutBrand = models.CharField(max_length=100,blank=True,null=True)
    aboutStorage = models.CharField(max_length=100,blank=True,null=True)
    qtyUnit = models.CharField(max_length=100,blank=True,null=True)
    aboutUsage = models.CharField(max_length=100,blank=True,null=True)
    aboutInstallation = models.CharField(max_length=100,blank=True,null=True)
    aboutHandling = models.CharField(max_length=100,blank=True,null=True)
    gstRate = models.CharField(max_length=100,blank=True,null=True)
    shippingMethod = models.CharField(max_length=100,blank=True,null=True)
    taxableAmount = models.CharField(max_length=100,blank=True,null=True)
    packagingSize = models.CharField(max_length=100,blank=True,null=True)
    components = models.CharField(max_length=100,blank=True,null=True)
    sla = models.CharField(max_length=100,blank=True,null=True)
    packedLength = models.CharField(max_length=100,blank=True,null=True)
    packedWidth = models.CharField(max_length=100,blank=True,null=True)
    packedHeight = models.CharField(max_length=100,blank=True,null=True)
    pickupLocation = models.CharField(max_length=100,blank=True,null=True)
    servicedRegions = models.CharField(max_length=100,blank=True,null=True)
    dimensionUnit = models.CharField(max_length=100,blank=True,null=True)
    variant = models.CharField(max_length=500,blank=True,null=True)
