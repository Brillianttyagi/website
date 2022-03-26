from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from requests.api import post
from inventory.models import Inventory
from inventory.models import PostPicture
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def current(request):
    orders = requests.get('https://api.seventhsq.com/orders/orders/seller/'+str(request.user.id))
    try:
        data = orders.json()
        for j,i in data.items():
            image = PostPicture.objects.filter(postid = i['product_no'])[0].picture
            shipped = Inventory.objects.get(id = i['product_no']).shippingMethod
            name = Inventory.objects.get(id = i['product_no']).name
            time = i['created_at']
            li = time.split('.')
            time = li[0]
            li = time.split('T')
            date = li[0]
            time  = datetime.strptime(li[1], "%H:%M:%S")
            time = time.strftime("%I:%M %p")
            i['created_at'] = str(time+' '+date)
            i['image'] = image
            i['name'] = name
            if shipped=='0':
                i['shipped'] = 'Self Shipping'
            else:
                i['shipped'] = 'Seventh Square Shipping'
        return render(request,'order/current.html',{'orders':data})
    except Exception as e:
        print(e)
        return render(request,'order/noorder.html')

@login_required
def older(request):
    orders = requests.get('https://api.seventhsq.com/orders/orders/seller/older/'+str(request.user.id))
    
    try:
        data = orders.json()
        print(data)
        for j,i in data.items():
            image = PostPicture.objects.filter(postid = i['product_no'])[0].picture
            shipped = Inventory.objects.get(id = i['product_no']).shippingMethod
            name = Inventory.objects.get(id = i['product_no']).name
            time = i['created_at']
            li = time.split('.')
            time = li[0]
            li = time.split('T')
            date = li[0]
            time  = datetime.strptime(li[1], "%H:%M:%S")
            time = time.strftime("%I:%M %p")
            i['created_at'] = str(time+' '+date)
            i['image'] = image
            i['name'] = name
            if shipped=='0':
                i['shipped'] = 'Self Shipping'
            else:
                i['shipped'] = 'Seventh Square Shipping'
        print(orders)
        return render(request,'order/order.html',{'orders':data})
    except Exception as e:
        print(e)
        return render(request,'order/noorder.html')
