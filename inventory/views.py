from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, Paginator
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from theseventhsquare.settings import MEDIA_URL

from inventory.models import Inventory

# Create your views here.

class InventoryList(View):
    template_name='inventory/list.html'
    def get(self,request,*args,**kwargs):
        inventory = Inventory.objects.filter(account=request.user)
        
        page_num = request.GET.get('page',1)
        try:
            paginated_inventory = Paginator(inventory,10).page(page_num)
        except EmptyPage:
            paginated_inventory = Paginator(inventory,10).page(1)
        return render(request,self.template_name,context={'inventory':paginated_inventory})
    def post(self,request,*args,**kwargs):
        return render(request,self.name)


class InventoryAdd(View):
    template_name='inventory/add.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    def post(self,request,*args,**kwargs):
        #do somthing here save data
        print(request.POST)
        # return HttpResponse('ok')
        data={
            'account':request.user,
            'name':request.POST.get("name"),
            'description':request.POST.get("description"),
            'image':request.FILES.get("image"),
            'category':request.POST.get("category"),
            'subCategory':request.POST.get("subCategory"),
            'HSN':request.POST.get("HSN"),
            'warranty':request.POST.get("warranty"),
            'guarantee':request.POST.get("guarantee"),
            'qty':request.POST.get("qty"),
            'length':request.POST.get("length"),
            'width':request.POST.get("width"),
            'height':request.POST.get("height"),
            'weight':request.POST.get("weight"),
            'marked':request.POST.get("marked"),
            'colors':request.POST.get("colors"),
            'material':request.POST.get("material"),
            'countryOfOrigin':request.POST.get("countryOfOrigin"),
            'inventoryStatus': "Live"==True if request.POST.get("inventoryStatus")else "Inactive"==False,
            'markedPrice':request.POST.get("markedPrice"),
            'sellingPrice':request.POST.get("sellingPrice"),
            'commercialPrice':request.POST.get("commercialPrice"),
            'aboutBrand':request.POST.get("aboutBrand"),
            'aboutStorage':request.POST.get("aboutStorage"),
            'qtyUnit':request.POST.get("qtyUnit"),
            'aboutUsage':request.POST.get("aboutUsage"),
            'aboutInstallation':request.POST.get("aboutInstallation"),
            'aboutHandling':request.POST.get("aboutHandling"),
            'gstRate':request.POST.get("gstRate"),
            'shippingMethod':request.POST.get("shippingMethod"),
            'taxableAmount':request.POST.get("taxableAmount"),
            'packagingSize':request.POST.get("packagingSize"),
            'components':request.POST.get("components"),
            'sla':request.POST.get("sla"),
            'packedLength':request.POST.get("packedLength"),
            'packedWidth':request.POST.get("packedWidth"),
            'packedHeight':request.POST.get("packedHeight"),
            'pickupLocation':request.POST.get("pickupLocation"),
            'servicedRegions':request.POST.get("servicedRegions"),
            'dimensionUnit':request.POST.get("dimensionUnit"),
            'variant':request.POST.get("variant"),
            }
        Inventory.objects.create(**data)
  
        return redirect('/inventory/add-new-product/')

class InventoryEdit(View):
    template_name='inventory/edit.html'
    def get(self,request,id,*args,**kwargs): 
        try:
            inventory = Inventory.objects.get(pk=id,account=request.user)
            return render(request,self.template_name,context={'inventory':inventory,'media':MEDIA_URL})
        except ObjectDoesNotExist:
            redirect('/inventory/active-products/')
    def post(self,request,id,*args,**kwargs):
        try:
            inventory = Inventory.objects.get(pk=id)
            inventory.account=request.user
            inventory.name = request.POST.get("name")
            inventory.description = request.POST.get("description")
            inventory.image = request.FILES.get("image")
            inventory.category = request.POST.get("category")
            inventory.subCategory = request.POST.get("subCategory")
            inventory.HSN = request.POST.get("HSN")
            inventory.warranty = request.POST.get("warranty")
            inventory.guarantee = request.POST.get("guarantee")
            inventory.qty = request.POST.get("qty")            
            inventory.length = request.POST.get("length")
            inventory.width = request.POST.get("width")
            inventory.height = request.POST.get("height")
            inventory.weight = request.POST.get("weight")
            inventory.marked = request.POST.get("marked")
            inventory.colors = request.POST.get("colors")
            inventory.material = request.POST.get("material")
            inventory.countryOfOrigin = request.POST.get("countryOfOrigin")
            inventory.inventoryStatus = True if request.POST.get("inventoryStatus")else False
            inventory.markedPrice = request.POST.get("markedPrice")
            inventory.sellingPrice = request.POST.get("sellingPrice")
            inventory.commercialPrice = request.POST.get("commercialPrice")
            inventory.aboutBrand=request.POST.get("aboutBrand")
            inventory.aboutStorage=request.POST.get("aboutStorage")
            inventory.qtyUnit=request.POST.get("qtyUnit")
            inventory.aboutUsage=request.POST.get("aboutUsage")
            inventory.aboutInstallation=request.POST.get("aboutInstallation")
            inventory.aboutHandling=request.POST.get("aboutHandling")
            inventory.gstRate=request.POST.get("gstRate")
            inventory.shippingMethod=request.POST.get("shippingMethod")
            inventory.taxableAmount=request.POST.get("taxableAmount")
            inventory.packagingSize=request.POST.get("packagingSize")
            inventory.components=request.POST.get("components")
            inventory.sla=request.POST.get("sla")
            inventory.packedLength=request.POST.get("packedLength")
            inventory.packedWidth=request.POST.get("packedWidth")
            inventory.packedHeight=request.POST.get("packedHeight")
            inventory.pickupLocation=request.POST.get("pickupLocation")
            inventory.servicedRegions=request.POST.get("servicedRegions")
            inventory.dimensionUnit=request.POST.get("dimensionUnit")
            inventory.variant=request.POST.get("variant")
            inventory.save()
            return redirect('/inventory/active-products/'+str(id)+'/')
        except ObjectDoesNotExist:
             return redirect('/inventory/active-products/')
        
class InventoryDelete(View):
    def get(self,request,*args,**kwargs):
        return redirect('/inventory/active-products/')
    def post(self,request,id,*args,**kwargs):
        try:
            inventory = Inventory.objects.get(pk=id)
            inventory.delete()
        except(ObjectDoesNotExist):
            pass
        return redirect('/inventory/active-products/')


class PreviewAct(View):
    template_name='previewact.html'
    def get(self,request,pk):
        inventory = Inventory.objects.filter(id=pk)
        
        return render(request,self.template_name,context={'inventory':inventory[0]})
    def post(self,request,*args,**kwargs):
        return render(request,self.name)