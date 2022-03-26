from os.path import join
from uuid import uuid4

from django.http import request

from account.models import Account
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid4(), ext)
    return join('inventory/', filename)




class Inventory(models.Model):
    #product regard field
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    name= models.CharField(max_length=200,blank=True,null=True)
    description = models.CharField(max_length=999,blank=True,null=True)
    category = models.CharField(max_length=100,blank=True,null=True)
    subCategory = models.CharField(max_length=100,blank=True,null=True)
    PostPicture = None
    HSN = models.CharField(max_length=100,blank=True,null=True)
    warranty = models.CharField(max_length=100,blank=True,null=True)
    guarantee = models.CharField(max_length=100,blank=True,null=True)
    length = models.CharField(max_length=100,blank=True,null=True)
    width = models.CharField(max_length=100,blank=True,null=True)
    height = models.CharField(max_length=100,blank=True,null=True)
    weight = models.FloatField(default=0)
    marked = models.CharField(max_length=100,blank=True,null=True)
    colors = models.CharField(max_length=100,default='',null=True,blank=True)
    material = models.CharField(max_length=255,blank=True,null=True)
    date = models.DateTimeField(default=timezone.now)
    countryOfOrigin = models.CharField(max_length=100,blank=True,null=True)

    #city = models.CharField(max_length=100,blank=True,null=True)
    inventoryStatus = models.BooleanField(default=True)
    shippingWithSeventhSquare = models.BooleanField(default=True)
    #inventory regard field
    qty = models.FloatField(validators=[MinValueValidator(0)])
    markedPrice = models.FloatField(validators=[MinValueValidator(0)])
    sellingPrice = models.FloatField(validators=[MinValueValidator(0)])
    commercialPrice = models.FloatField(validators=[MinValueValidator(0)], default=0.0, blank=True,null=True)
    discount = models.IntegerField(null=True)
    aboutBrand = models.CharField(max_length=999,blank=True,null=True)
    aboutStorage = models.CharField(max_length=999,blank=True,null=True)
    qtyUnit = models.CharField(max_length=999,blank=True,null=True)
    aboutUsage = models.CharField(max_length=999,blank=True,null=True)
    aboutInstallation = models.CharField(max_length=999,blank=True,null=True)
    aboutHandling = models.CharField(max_length=999,blank=True,null=True)
    gstRate = models.CharField(max_length=100,blank=True,null=True)
    shippingMethod = models.CharField(max_length=100,blank=True,null=True)
    taxableAmount = models.CharField(max_length=100,blank=True,null=True)
    packagingSize = models.CharField(max_length=100,blank=True,null=True)
    components = models.CharField(max_length=255,blank=True,null=True)
    sla = models.CharField(max_length=100,blank=True,null=True)
    packedLength = models.CharField(max_length=100,blank=True,null=True)
    packedWidth = models.CharField(max_length=100,blank=True,null=True)
    packedHeight = models.CharField(max_length=100,blank=True,null=True)
    pickupLocation = models.CharField(max_length=100,blank=True,null=True)
    servicedRegions = models.CharField(max_length=100,blank=True,null=True)
    dimensionUnit = models.CharField(max_length=100,blank=True,null=True)
    variant = models.CharField(max_length=999,blank=True,null=True)
    product_tags = TaggableManager(verbose_name="product_tags",blank=True)
    brand_name = models.CharField(max_length=30)
    incl_gst = models.BooleanField(default=False)
    incl_shipping = models.BooleanField(default=False)

class PostPicture(models.Model):
    picture = models.ImageField(get_file_path, blank=True)
    postid = models.ForeignKey(Inventory,on_delete=models.CASCADE)

class ServiceRegionOfSeller(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    region = models.CharField(max_length=100)
    cost = models.CharField(max_length=1000)
    time_of_delivery = models.CharField(max_length=100)