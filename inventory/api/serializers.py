from django.db.models import fields
from django.db.models.fields import files
from rest_framework import serializers
from inventory.models import Inventory,PostPicture,ServiceRegionOfSeller


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id','account','name','description','category','subCategory','HSN','warranty','guarantee','length','width','height','weight','marked','colors','material','date','countryOfOrigin','inventoryStatus','shippingWithSeventhSquare','qty','markedPrice','sellingPrice','discount','commercialPrice','aboutBrand','aboutStorage','qtyUnit','aboutUsage','aboutInstallation','aboutHandling','gstRate','shippingMethod','taxableAmount','packagingSize','components','sla','packedLength','packedWidth','packedHeight','pickupLocation','servicedRegions','dimensionUnit','variant','brand_name','incl_gst']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostPicture
        fields = ['picture']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceRegionOfSeller
        fields = '__all__'