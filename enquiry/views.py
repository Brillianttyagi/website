from django.shortcuts import redirect, render
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
import requests
from requests.api import post
from datetime import datetime
from django.contrib.auth.decorators import login_required
from inventory.models import Inventory
from inventory.models import PostPicture
from account.models import Account

@login_required
def quotation(request):
    orders = requests.get('https://api.seventhsq.com/enquiry/seller/get/'+str(request.user.id))
    try:
        data = orders.json()
        for i in data:
            name = Inventory.objects.get(id = i['product_id']).name
            i['name'] = name
        return render(request,'enquiry/quotation.html',{'enquiry':data})
    except Exception as e:
        print(e)
        return render(request,'order/noorder.html')

@login_required
def reply(request):
    enquiry_id =request.POST.get('enquiry_id')
    message =request.POST.get('message')
    data = {
    
    "token":"54ertyuioplkjhgtr567890ytwerdfghbiohj",
    "enquiry_id":str(enquiry_id),
    "message":str(message)
    }
    
    orders = requests.post('https://api.seventhsq.com/enquiry/email/quotation',data=data)
    return redirect('/enquiry/details')    


#proposal
@login_required
def proposal(request):
    orders = requests.get('https://api.seventhsq.com/enquiry/seller/proposal/get/'+str(request.user.id))
    try:
        data = orders.json()
        for i in data:
            name = Inventory.objects.get(id = i['product_id']).name
            i['name'] = name
        return render(request,'enquiry/proposal.html',{'enquiry':data})
    except Exception as e:
        print(e)
        return render(request,'order/noorder.html')

@login_required
def proposalreply(request):
    enquiry_id =request.POST.get('enquiry_id')
    message =request.POST.get('message')
    data = {
    
    "token":"54ertyuioplkjhgtr567890ytwerdfghbiohj",
    "enquiry_id":str(enquiry_id),
    "message":str(message)
    }
    
    orders = requests.post('https://api.seventhsq.com/enquiry/email/proposal',data=data)
    return redirect('/enquiry/proposal')     
 

#information
@login_required
def information(request):
    orders = requests.get('https://api.seventhsq.com/enquiry/seller/information/get/'+str(request.user.id))
    try:
        data = orders.json()
        for i in data:
            name = Inventory.objects.get(id = i['product_id']).name
            i['name'] = name
        return render(request,'enquiry/information.html',{'enquiry':data})
    except Exception as e:
        print(e)
        return render(request,'order/noorder.html')

@login_required
def informationreply(request):
    enquiry_id =request.POST.get('enquiry_id')
    message =request.POST.get('message')
    data = {
    
    "token":"54ertyuioplkjhgtr567890ytwerdfghbiohj",
    "enquiry_id":str(enquiry_id),
    "message":str(message)
    }
    
    orders = requests.post('https://api.seventhsq.com/enquiry/email/info',data=data)
    return redirect('/enquiry/information')     

#bpo
@login_required
def bpo(request):
    orders = requests.get('https://api.seventhsq.com/enquiry/seller/bpo/get/'+str(request.user.id))
    try:
        data = orders.json()
        for i in data:
            name = Inventory.objects.get(id = i['product_id']).name
            i['name'] = name
        return render(request,'enquiry/bpo.html',{'enquiry':data})
    except Exception as e:
        print(e)
        return render(request,'order/noorder.html')

@login_required
def bporeply(request):
    enquiry_id =request.POST.get('enquiry_id')
    message =request.POST.get('message')
    data = {
    
    "token":"54ertyuioplkjhgtr567890ytwerdfghbiohj",
    "enquiry_id":str(enquiry_id),
    "message":str(message)
    }
    
    orders = requests.post('https://api.seventhsq.com/enquiry/email/bpo',data=data)
    return redirect('/enquiry/bpo')       
      

@login_required
def admin_main(request):
    if request.user.is_superuser:
        orders = requests.get('https://api.seventhsq.com/enquiry/email/54ertyuioplkjhgtr567890ytwerdfghbiohj/main')
        try:
            data = orders.json()
            emails = Account.objects.all()
            li = {}
            for i in emails:
                li[str(i.Representativename)]=i.email
            
            print(data)
            return render(request,'enquiry/adminmain.html',{'enquiry':data,'emails':li})
        except Exception as e:
            print(e)
            return render(request,'order/noorder.html')
    else:
        raise Http404

@login_required
def admin_main_reply(request):
    
    
    try:
        product_id = request.POST.get('product_id')
        emails = request.POST.get('email[]')
        category=request.POST.get('category')
        phone=request.POST.get('phone')
        brand_preference=request.POST.get('brand_preference')
        desc=request.POST.get('desc')
        quantity_required=request.POST.get('quantity_required')
        delivery_location=request.POST.get('delivery_location')
        delivery_timeline=request.POST.get('delivery_timeline')
        bemail=request.POST.get('bemail')
        id =request.POST.get('id')
        message =request.POST.get('message')
        subject = request.POST.get('subject')
        li = {}
        emails = [emails]
        for i in emails:
            mail = Account.objects.get(email = i)
            data = {
                "product_id": product_id,
                "category": category,
                "phone": phone,
                "brand_preference": brand_preference,
                "desc": desc,
                "quantity_required": quantity_required,
                "delivery_location": delivery_location,
                "delivery_timeline": delivery_timeline,
                "seller": mail.id,
                "email": bemail
            }
            
            data2 = {
                "id":int(id),
                "message":message,
                "subject":subject,
                "email": str(i),
                "token":"54ertyuioplkjhgtr567890ytwerdfghbiohj"
            }
            orders = requests.post('https://api.seventhsq.com/enquiry/email/post/main/',data=data2)
            x = requests.post('https://api.seventhsq.com/enquiry/request/',data=data)

        return redirect('/enquiry/admin_main_enquiry')
    except Exception as e:
        print(e)
        return render(request,'enquiry/adminmain.html')