import os

from address.models import Address
from bank.models import Bank
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import FileResponse, Http404, HttpResponse
from django.shortcuts import redirect, render
from theseventhsquare.settings import BASE_DIR, MEDIA_URL

from account.models import Account


def Profile(request):
    account = Account.objects.get(pk=request.user.id)
    bank = Bank.objects.filter(account=request.user.id).first()
    
    addressCompany = Address.objects.filter(account=request.user,addressType='COMPANY').first()
    if addressCompany is None:
        addressCompany={} 
    addressRepresentative = Address.objects.filter(account=request.user,addressType='REPRESENTATIVE').first()
    if addressRepresentative is None:
        addressRepresentative={} 
    context={
        'account':account,
        'addressCompany':addressCompany,
        'addressRepresentative':addressRepresentative,
        'bank' : bank,
        'REPR_CHOICES':Account.REPR_CHOICES,
        'COMAPNY_CATEGORY':Account.COMAPNY_CATEGORY,
        'DOC_TYPE_CHOIES':Account.DOC_TYPE_CHOIES,
        'BANK_CHOICES':Bank.BANK_CHOICES,
        'STATE_CHOICES':Address.STATE_CHOICES,
        'media_url':MEDIA_URL
    }
    print(account.Representativeimage.name,'ss')
    return render(request,template_name='account/profile.html',context=context)

def KYCDocFileDownload(request,companykycdoc):
    if request.user.is_authenticated:
        try:
            return FileResponse(request.user.companyKYCDOC.file)
        except FileNotFoundError:
            raise Http404
def GSTDocFileDownload(request,gstdoc):
    if request.user.is_authenticated:
        try:
            return FileResponse(request.user.GSTDoc.file)
        except FileNotFoundError:
            raise Http404
