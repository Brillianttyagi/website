import utility
from communication import communication
from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Account


class Register(View):
    template_name = 'account/register.html'
    template_name_otp =  'account/otp.html'
    def get(self,request,*args,**kwargs):
        return render(request,template_name=self.template_name)

    def post(self,request,*args,**kwargs):
        verificationCode=utility.randomString(5)
        data = {
        'username':request.POST.get('mobileNumber'),
        'Representativename' : request.POST.get('Representativename'),
        'companyName' : request.POST.get('companyName'),
        'email' : request.POST.get('email'),
        'mobileNumber' : request.POST.get('mobileNumber'),
        'emailVerificationCode' : verificationCode,
        'mobileVerificationCode' : verificationCode,
        'password' : request.POST.get('password'),
        'companyGSTNumber' : request.POST.get('companyGSTNumber'),
        }
        if 'mobile' in request.session and request.session['mobile']==request.POST.get('mobileNumber') and request.session['otp']==request.POST.get('OTP'):
            data['isMobileNumberVerified'] = True
        try:
            account=Account(**data)
            account.set_password(data['password'])
            account.full_clean()
            account.save()
            communication.send(request,'register',email=account.email,user=account.pk,otp=verificationCode)
            if not account.isMobileNumberVerified:
                return render(request,template_name=self.template_name_otp,context={'account':account.pk})
            else:
                #if user is verified has mobile number then forward to login
                login(request,account)
                return redirect('/account/gstindetail/')
                
        except IntegrityError:
            # mobile and email is unique
            print(IntegrityError)
            message = "Either Email or Mobile Number is Already Registered !!"
            color = "danger"
            return render(request,self.template_name,{'message':message,'color':color})
        except ValidationError as err:
            message = "Validation error!!"
            color = "danger"
            print(err.message_dict.items())
            return render(request,self.template_name,{'message':message,'color':color,'error':err})

class Confirmation(View):
    def get(self,request,*args,**kwargs):
        emailVerificationCode = request.GET.get('emailVerificationCode')
        mobileVerificationCode = request.GET.get('mobileVerificationCode')
        account =request.GET.get('account')
        try:
            account = Account.objects.get(pk=account)
            update=[]
            if account.mobileVerificationCode is not None and account.mobileVerificationCode == mobileVerificationCode and account.mobileVerificationCode!='':
                account.isMobileNumberVerified=True
                update.append('isMobileNumberVerified')
            if account.emailVerificationCode is not None and account.emailVerificationCode == emailVerificationCode and account.emailVerificationCode!='':
                account.isEmailVerified=True
                update.append('isEmailVerified')
            if len(update)>0:
                account.save(update_fields=update)
                return HttpResponse('account verified sucessfully <a href="/account/">login</a>')
            else:
                return HttpResponse('validation fail <a href="/account/">login</a>')
        except ObjectDoesNotExist:
            return HttpResponse('validation fail <a href="/account/">login</a>')
        
class Login(View):
    template_name = 'account/login.html'
    def get(self,request,*args,**kwargs):
        print(request.user)
        return render(request,template_name=self.template_name)
    def post(self,request,*args,**kwargs):
        data={
            'email':request.POST.get('mobileNumber'),
            'mobileNumber' : request.POST.get('mobileNumber') 
        }
        password = request.POST.get('password') 
        otp = request.POST.get('otp')
        try:
            account = Account.objects.get(Q(email=data['email'])| Q(mobileNumber=data['mobileNumber']))
            if (password is not None and account.check_password(password)) or (otp is not None and account.mobileVerificationCode==otp):
                login(request,account)
                return redirect('/')
            else:
                message='Password is incorrect' if not otp else "OTP is incorrect"
                color = 'danger'
                return render(request,template_name=self.template_name,context={'color':color,'message':message})
        except ObjectDoesNotExist:
            message='The account does not exist'
            color='danger'
            return render(request,template_name=self.template_name,context={'color':color,'message':message})
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('/account/login')

    def post(self,request):
        logout(request)
        return redirect('/account/login')

class Forget(View):
    template_name = 'account/forget.html'

    def get(self,request,*args,**kwargs):
        return render(request,template_name=self.template_name)
    def post(self,request,*args,**kwargs):
        data={
            'email':request.POST.get('mobileNumber'),
            'mobileNumber' : request.POST.get('mobileNumber') 
        }
        try:
            account = Account.objects.get(Q(email=data['email'])| Q(mobileNumber=data['mobileNumber']))
            verificationCode=utility.randomString(5)
            account.emailVerificationCode = verificationCode
            account.mobileVerificationCode = verificationCode
            account.save()
            communication.send(request,'forget',mobile=account.mobileNumber,email=account.email,user=account.pk,otp=verificationCode)
            message='A password is sended to your Email  and Mobile'
            color = 'info'
            return render(request,template_name=self.template_name,context={'color':color,'message':message})
        except ObjectDoesNotExist:
            message='The account does not exist. please enter a valid email/mobile number'
            color='danger'
            return render(request,template_name=self.template_name,context={'color':color,'message':message})

@csrf_exempt
@require_http_methods(['POST'])
def send_login_otp(request):
    data={
            'email':request.POST.get('mobileNumber'),
            'mobileNumber' : request.POST.get('mobileNumber') 
        }
    try:
        account = Account.objects.get(Q(email=data['email'])| Q(mobileNumber=data['mobileNumber']))
        verificationCode=utility.randomString(5)
        account.emailVerificationCode = verificationCode
        account.mobileVerificationCode = verificationCode
        account.save()
        communication.send(request,'sendOtpLogin',mobile=account.mobileNumber,email=account.email,user=account.pk,otp=verificationCode)
        return HttpResponse('otp sended')
    except ObjectDoesNotExist:
        return HttpResponse('user not found',status=404)
        
@csrf_exempt
@require_http_methods(['POST'])
def send_mobile_otp(request):
    if Account.objects.filter(mobileNumber = request.POST.get('mobileNumber')).exists():
        return HttpResponse('User Already Registered with ' + request.POST.get('mobileNumber'),status = 400)
        
    mobileNumber = request.POST.get('mobileNumber') 
    otp = utility.randomString(5)
    request.session['otp']=otp
    request.session['mobile']=mobileNumber
    communication.send(request,'sendmobileotp',mobile=mobileNumber,otp=otp)
    return HttpResponse('otp sended')
        
@csrf_exempt
@require_http_methods(['POST'])      
def verify_mobile_otp(request):
    if (('otp' in request.session and request.session['otp']==request.POST.get('otp')) and 
        ('mobile' in request.session and request.session['mobile']==request.POST.get('mobileNumber'))):
        return HttpResponse('otp is verified')
    else:
        return HttpResponse('otp verification fail',status=400)
