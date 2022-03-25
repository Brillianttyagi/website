from django.shortcuts import redirect, render
from django.views import View

from account.models import Account
from .background import fetch_gstin_detail

class EntityDetail(View):
    template_name=''
    def get(self,request,*args,**kwargs):
        return  redirect('/account/')
    def post(self,request):
        companyGSTNumber = request.POST.get('companyGSTNumber')
        GSTDoc = request.FILES.get('GSTDoc')
        companyKYCDocType = request.POST.get('companyKYCDocType')
        companyKYCDOC = request.FILES.get('companyKYCDOC')
        account = Account.objects.get(pk=request.user.id)
        print(request.POST,request.FILES)
        
        old_gtin_number = account.companyGSTNumber

        if companyGSTNumber !='':
            account.companyGSTNumber = companyGSTNumber
        if companyKYCDocType !='':
            account.companyKYCDocType = companyKYCDocType
        if companyKYCDOC is not None and companyKYCDOC !='':
            account.companyKYCDOC = companyKYCDOC
        if GSTDoc is not None and GSTDoc !='':
            account.GSTDoc = GSTDoc
        try:
            account.save()
            if(account.companyGSTNumber != old_gtin_number):
                fetch_gstin_detail(gstin_number=account.companyGSTNumber,user_id=account.id)
        except(Exception):
            pass
        return  redirect('/account/')
