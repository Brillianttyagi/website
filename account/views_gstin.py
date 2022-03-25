from django.shortcuts import redirect, render
from django.views import View

from account.models import Account
from .background import fetch_gstin_detail

class GSTINDetail(View):
    template_name='account/gstin.html'
    def get(self,request,*args,**kwargs):
        return  render(request,template_name=self.template_name)
    def post(self,request):
        companyGSTNumber = request.POST.get('companyGSTNumber')
        account = Account.objects.get(pk=request.user.id)
        if companyGSTNumber !='':
            account.companyGSTNumber = companyGSTNumber
        try:
            account.save()
            fetch_gstin_detail(gstin_number=account.companyGSTNumber,user_id=account.id)
        except(Exception):
            pass
        return  redirect('/account/generaldetail/')
