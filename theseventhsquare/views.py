import datetime
import secrets
import urllib.request
from random import randint
from theseventhsquare.settings import EMAILS
from account.models import Account
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives, send_mail
from django.core.paginator import EmptyPage, Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import View
from seller.models import (Bank_verify, Entity_verify, New_sup, Notify,
                           Products, Representative_verify, S_prod)

from theseventhsquare.settings import ap
from background_task import background
from faq.models import Faq
from blog.models import Blog
from forum.models import TalkToUs,RequestACallback

ottp = str()

def home(request):
    if not request.user.is_authenticated:
        return render(request,'seller_index.html')
    else:
        return render(request,'dashboard.html')


#search bar
def search(request):
    query = request.GET['query']
    faq_posts = Faq.objects.all().filter(question__icontains=query)
    blog_posts= Blog.objects.all().filter(title__icontains=query)
    faq_bposts = Faq.objects.all().filter(answer__icontains=query)
    blog_bposts= Blog.objects.all().filter(body__icontains=query)
    li = []
    blog_li = []
    for i in faq_posts:
        li.append(i)
    for i in faq_bposts:
        if i not in li:
            li.append(i)
    #for blog
    for i in blog_posts:
        blog_li.append(i)
    for i in blog_bposts:
        if i not in blog_li:
            blog_li.append(i)
    return render(request, 'search.html', {'faq' : li, 'blog': blog_li })   


def notifica(a,b,sup_id):
    notif = Notify.objects.get(sup_id=sup_id)
    notif.n3=notif.n2
    notif.n2=notif.n1
    notif.n1=a
    notif.s3=notif.s2
    notif.s2=notif.s1
    notif.s1=800
    notif.l3=notif.l2
    notif.l2=notif.l1
    notif.l1=b
    notif.coun+=1
    notif.save()
    return 0



def index(request):
    if request.session.get('sup_id'):
        obj = New_sup.objects.get(sup_id=request.session.get('sup_id'))
        nam = obj.name
        nam = nam.split(' ')[0]
        pr = S_prod.objects.filter(sup_id=request.session.get('sup_id'),prod_status="Active")
        notif = Notify.objects.get(sup_id=request.session.get('sup_id'))
        return render(request,'dashboard.html',{'nam':nam,'loca':obj,'notif':notif,'l':len(pr)})
    else:
        return render(request,'s_register.html')


def notify_read(request):
    sup_id = request.session.get('sup_id')
    notif = Notify.objects.get(sup_id=sup_id)
    notif.s1=400
    notif.s2=400
    notif.s3=400
    notif.coun=0
    notif.save()
    return redirect('/')

def about(request):
    return render(request,'about.html')

def careers(request):
    return render(request,'careers.html')

def comterm(request):
    return render(request,'comterm.html')

def selguide(request):
    return render(request,'selguide.html')

def contact(request):
    return render(request,'s_contact.html')

def aftercontact(request):
    name = request.POST.get('fname')
    phn = request.POST.get('phonenumber')
    email = request.POST.get('email')
    subj = request.POST.get('subj')
    msg = request.POST.get('msg')
    subject = "We have a query from seller"
    message = f"Name : {name}\nPhone : {phn}\nEmail : {email}\nSubject : {subj}\n\nMessage : {msg}"
    to_email = "seller@seventhsq.com"
    send_mail(subject,message,settings.EMAIL_HOST_USER,[to_email],auth_password=settings.EMAIL_HOST_PASSWORD)
    b = notifica("You Will Get An Update For Your Query Within 24-48 Hours","/contact/",request.session.get('sup_id'))
    notif = Notify.objects.get(sup_id=request.session.get('sup_id'))
    msg = "We will resolve your query within 48 hours."
    col = "info"
    return render(request,'s_contact.html',{'notif':notif,'msg':msg,'col':col})

@background(queue='email',schedule=1)
def sendcallbackus(subject,message,*args,**kwargs):
    send_mail(subject,message,EMAILS['team'],EMAILS['no_reply'],fail_silently=False)

def callbackus(request):

    email = request.POST.get('email')
    msg = request.POST.get('msg')
    obj = TalkToUs.objects.create(contact=email,desc = msg)
    obj.save()
    subject = "We have a query from seller"
    message = f"Email : {email}\nMessage : {msg}"
    to_email = "seller@seventhsq.com"
    sendcallbackus(subject,message)
    return redirect("/")

def requestacallback(request):
    mobile = request.POST.get('contact')
    name = request.POST.get('name')
    obj = RequestACallback.objects.create(name=name,cont = mobile)
    obj.save()
    subject = "We have a query from seller"
    message = f"Name : {name}\nConatact : {mobile}"
    to_email = "seller@seventhsq.com"
    sendcallbackus(subject,message)
    return redirect("/")


def partner(request):
    return render(request,'dash-partner.html')

def afterpartner(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    numb = request.POST.get('numb')
    msg = request.POST.get('msg')
    subject = "Partner with us message"
    to_email = "partners@seventhsq.com"
    message = f"Name : {name}\nEmail : {email}\nContact : {numb}\n\n{msg}"
    send_mail(subject,message,settings.EMAIL_HOST_USER,[to_email],auth_password=settings.EMAIL_HOST_PASSWORD)
    return render(request,'dash-partner.html')

def corporate(request):
    return render(request,'corporate.html')

def aftercorporate(request):
    name = request.POST.get('name')
    numb = request.POST.get('numb')
    subject = "We Have A Call Request"
    to_email = "corporate@seventhsq.com"
    message = f"Name : {name}\nContact : {numb}"
    send_mail(subject,message,settings.EMAIL_HOST_USER,[to_email],auth_password=settings.EMAIL_HOST_PASSWORD)
    return render(request,'corporate.html')

def policy(request):
    return render(request,'dash-policy.html')

def marketplace(request):
    image_data = open("policy/marketplace.pdf","rb").read()
    return HttpResponse(image_data, content_type="application/pdf")

def terms(request):
    image_data = open("policy/terms.pdf","rb").read()
    return HttpResponse(image_data, content_type="application/pdf")

def coming(request):
    notif = Notify.objects.get(sup_id=request.session.get('sup_id'))
    return render(request,'coming-soon.html',{'notif':notif})


def pricecalculator(request):
    return render(request,'price.html')

def shippingamount(a):
    if a <= 500:return 50
    elif a <= 1000:return 82.5
    elif a <= 1500:return 120
    elif a <= 2000:return 157.5
    elif a <= 2500:return 195
    elif a <= 3000:return 232.5
    elif a <= 4000:return 270
    elif a <= 5000:return 307.5
    elif a <= 6000:return 345
    elif a <= 7000:return 382.5
    elif a <= 8000:return 420
    elif a <= 9000:return 457.5
    elif a <= 10000:return 495
    elif a <= 11000:return 532.5
    elif a <= 12000:return 575
    else:return ((((a-12000)//1000)+((a-12000)%1000>0))*37.5)+575

def dash_new(request):
    if request.session.get('sup_id'):
        notif = Notify.objects.get(sup_id=request.session.get('sup_id'))
        data = New_sup.objects.get(sup_id=request.session.get('sup_id'))
        return render(request,'dash-new.html',{'notif':notif,'data':data})
    else:
        return redirect('/login/')

def after_new(request):
    data={
        'desc' : request.POST.get('desc'),
        'heading' : request.POST.get('heading'),
        'category' : request.POST.get('cate'),
        'sub_c' : request.POST.get('sub_c'),
        'city' : request.POST.get('city'),
        'country' : request.POST.get('coo'),
        'hsn' : request.POST.get('hsn'),
        'warranty' : request.POST.get('war'),
        'guarantee' : request.POST.get('gua'),
        'inventory' : request.POST.get('inven'),
        'about' : request.POST.get('about'),
        'prod_l' : request.POST.get('pl'),
        'prod_w' : request.POST.get('pw'),
        'prod_h' : request.POST.get('ph'),
        'box_l' : request.POST.get('bl'),
        'box_w' : request.POST.get('bw'),
        'box_h' : request.POST.get('bh'),
        's_weight' : request.POST.get('s_weight'),
        'colour' : request.POST.get('colo'),
        'size' : request.POST.get('siz'),
        'material' : request.POST.get('mat'),
        'marked' : request.POST.get('mp'),
        'listed' : request.POST.get('lp'),
        'disbursement' : request.POST.get('ip'),
    }
    sh = request.POST.get('sh')
    if sh == 'on':
        ob = int(data['box_l'])*int(data['box_w'])*int(data['box_h'])/4000
        if ob < float(data['s_weight']):
            s = shippingamount(float(data['s_weight']))
        else:s = shippingamount(ob)
    else:s = 0
    data['sale'] = (float(data['disbursement'])+s)/0.911
    ob = New_sup.objects.get(sup_id=request.session.get('sup_id'))
    data['sup_id'] = ob
    if data['inventory'] == '':data['inventory']=0
    if data['prod_l']=='' or data['prod_w']=='' or data['prod_h']=='':notifica("Some fields of your new product are empty","/viewproducts/",ob.sup_id)
    prod_img = request.FILES.getlist('prodimg')
    # print(prod_img)
    yo = request.POST.get('yo')
    obj = Products.objects.get(na='Prods')
    if prod_img!=[]:
        ur = ''
        a = obj.productimg
        for i in prod_img:
            fs = FileSystemStorage()
            fs.save(f'{a}.jpg',i)
            ur+=fs.url(f'{a}.jpg')
            a+=1
            ur+='|'
        data['prod_img'] = ur
        data['frstimg'] = data['prod_img'][:data['prod_img'].index("|")]
        data['prod_img'] = ur.strip('|')
        obj.productimg = a
    # print(data['frstimg'])
    pr = obj.product
    data['prod_id'] = ob.sup_id+'-'+data['category']+'-'+(str(obj.product).zfill(7))
    new_obj = S_prod.objects.create(**data)
    new_obj.save()
    obj.product += 1
    obj.save()
    data = request.session.get('sup_id')
    # if yo == 'on':
    #     subject = "New product added!"
    #     message =  f"Your new product is added successfully!! \n\n Product Description: {data['desc']}\n Product Heading: {data['heading']}\n Category: {data['category']}\n Sub Category: {data['sub_c']}\n Location: {data['city']}\n Country Of Origin: {data['country']}\n HSN Code: {data['hsn']}\n Inventory With Us: {data['inventory']}\n Product Length: {data['prod_l']}\n Product Width: {data['prod_w']}\n Product Height: {data['prod_h']}\n Box Length: {data['box_l']}\n Box Width: {data['box_w']}\n Box Height: {data['box_h']}\n Product Weight: {data['s_weight']}\n Product Colour: {data['colour']}\n Product Material: {data['material']}\n Marked Price: {data['marked']}\n Listed Price: {data['listed']}\n Commercial Price (Seller): {data['sale']}\n Selling Price SS: {data['disbursement']}"
    #     to_email = ob.email
    #     send_mail(subject,message,settings.EMAIL_HOST_USER,[to_email],auth_password=settings.EMAIL_HOST_PASSWORD)
    msg = "New Product Added."
    col = "success"
    x = notifica('Added A New Product',"/viewproducts/",data)
    notif = Notify.objects.get(sup_id=request.session.get('sup_id'))
    return render(request,'dash-new.html',{'notif':notif,'msg':msg,'col':col})

def preview(request,prod):
    data = S_prod.objects.get(sup_id=request.session.get('sup_id'),prod_id=prod)
    ll = data.prod_img.split('|')[1:]
    return render(request,'preview.html',{'data':data,'ll':ll})

def dlt_new(request,dl):
    data = S_prod.objects.get(sup_id=request.session.get('sup_id'),prod_id=dl)
    data.prod_status = ''
    data.save()
    x = notifica('Product Removed',"/viewproducts/",data.sup_id)
    return redirect('/viewproducts/')

def dash_view(request):
    if request.session.get('sup_id'):
        pr = S_prod.objects.filter(sup_id=request.session.get('sup_id')).exclude(prod_status="").order_by('-date')
        page_num = request.GET.get('page',1)
        try:
            p = Paginator(pr,10).page(page_num)
        except EmptyPage:
            p = Paginator(pr,10).page(1)
        notif = Notify.objects.get(sup_id=request.session.get('sup_id'))
        return render(request,'dash-view.html',{'data':p,'l':len(pr),'notif':notif})
    else:
        return redirect('/login/')

def edit_view(request,title):
    data = S_prod.objects.get(sup_id=request.session.get('sup_id'),prod_id=title)
    notif = Notify.objects.get(sup_id=request.session.get('sup_id'))
    name = New_sup.objects.get(sup_id=request.session.get('sup_id')).name
    return render(request,'dash-editnew.html',{'data':data,'notif':notif,'name':name})

def edit_new(request,prod):
    data = S_prod.objects.get(prod_id=prod)
    data.desc = request.POST.get('desc')
    data.heading = request.POST.get('heading')
    data.category = request.POST.get('cate')
    data.sub_c = request.POST.get('sub_c')
    data.city = request.POST.get('city')
    data.country = request.POST.get('coo')
    data.hsn = request.POST.get('hsn')
    data.warranty = request.POST.get('war')
    data.guarantee = request.POST.get('gua')
    data.inventory = request.POST.get('inven')
    data.about = request.POST.get('about')
    data.prod_l = request.POST.get('pl')
    data.prod_w = request.POST.get('pw')
    data.prod_h = request.POST.get('ph')
    data.box_l = request.POST.get('bl')
    data.box_w = request.POST.get('bw')
    data.box_h = request.POST.get('bh')
    data.s_weight = request.POST.get('s_weight')
    data.colour = request.POST.get('colo')
    data.size = request.POST.get('siz')
    data.material = request.POST.get('mat')
    data.marked = request.POST.get('mp')
    data.listed = request.POST.get('lp')
    data.disbursement = request.POST.get('ip')
    ob = float(data.box_l)*float(data.box_w)*float(data.box_h)/4000
    if ob < float(data.s_weight):
        s = shippingamount(float(data.s_weight))
    else:s = shippingamount(ob)
    data.sale = (float(data.disbursement)+s)/0.911
    if data.inventory == '':data.inventory=0
    if data.prod_l or data.prod_w or data.prod_h=='':notifica("Some fields of your updated product are empty","/viewproducts/",data.sup_id)
    prod_img = request.FILES.getlist('prodimg')
    yo = request.POST.get('yo')
    obj = Products.objects.get(na='Prods')
    if prod_img!=[]:
        ur = ''
        a = obj.productimg
        for i in prod_img:
            fs = FileSystemStorage()
            fs.save(f'{a}.jpg',i)
            ur+=fs.url(f'{a}.jpg')
            a+=1
            ur+='|'
        data.prod_img = ur
        data.frstimg = data.prod_img[:data.prod_img.index("|")]
        data.prod_img = ur.strip('|')
        obj.productimg = a
        obj.save()
    data.save()
    # if yo == 'on':
    #     subject = "Product Editted!"
    #     message =  f"Your product is changed successfully!! \n\n Product Description: {data.desc}\n Product Heading: {data.heading}\n Category: {data.category}\n Sub Category: {data.sub_c}\n Location: {data.city}\n Country Of Origin: {data.country}\n HSN Code: {data.hsn}\n Inventory With Us: {data.inventory}\n Product Length: {data.prod_l}\n Product Width: {data.prod_w}\n Product Height: {data.prod_h}\n Box Length: {data.box_l}\n Box Width: {data.box_w}\n Box Height: {data.box_h}\n Product Weight: {data.s_weight}\n Product Colour: {data.colour}\n Product Material: {data.material}\n Marked Price: {data.marked}\n Listed Price: {data.listed}\n Commercial Price (Seller): {data.sale}\n Selling Price SS: {data.disbursement}"
    #     to_email = New_sup.objects.get(sup_id=data.sup_id).email
    #     send_mail(subject,message,settings.EMAIL_HOST_USER,[to_email],auth_password=settings.EMAIL_HOST_PASSWORD)
    x = notifica('Successfully Updated A Product',"/viewproducts/",data.sup_id)
    return redirect('/viewproducts/')


