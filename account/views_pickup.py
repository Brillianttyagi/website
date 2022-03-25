from pickup.models import Pickup
from django.shortcuts import redirect
from django.views import View

class PickupDetail(View):
    template_name=''
    def get(self,request,*args,**kwargs):
        return  redirect('/account/')
    def post(self,request):
        pickupPlotNo = request.POST.get('pickupplotno')
        pickupStreet = request.POST.get('pickupstreet')
        pickupCity = request.POST.get('pickupcity')
        pickupState = request.POST.get('pickupstate')
        pickupPin = request.POST.get('pickuppin')
        print(request.POST)
        
        if pickupPlotNo !='':
            Pickup.pickupPlotNo = pickupPlotNo
        if pickupStreet !='':
            Pickup.pickupStreet = pickupStreet
        if pickupCity !='':
            Pickup.pickupCity = pickupCity
        if pickupState !='':
            Pickup.pickupState = pickupState
        if pickupPin !='':
            Pickup.pickupPin = pickupPin
        return  redirect('/account/')
