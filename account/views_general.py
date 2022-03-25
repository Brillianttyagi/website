from django.shortcuts import redirect, render
from django.views import View

from account.models import Account


class GeneralDetail(View):
    template_name='account/general.html'
    def get(self,request,*args,**kwargs):
        return  render(request,template_name=self.template_name)
    def post(self,request):
        companyName = request.POST.get('companyName')
        Representativename = request.POST.get('Representativename')
        city = request.POST.get('city')
        account = Account.objects.get(pk=request.user.id)
        
        if companyName !='':
            account.companyName = companyName
        if Representativename !='':
            account.Representativename = Representativename
        if city !='':
            account.city = city
        try:
            account.save()
        except(Exception):
            pass
        print(request.POST,request.FILES)
        return  redirect('/')
