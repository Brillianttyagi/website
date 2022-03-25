from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from seller.models import New_sup, Products

from .models import Comment, Discussion


def forum(request):
    obj = Discussion.objects.values()
    return render(request,'forum/forum.html',{'data':obj})

def disc(request,prod):
    data = Discussion.objects.get(pk=prod)
    data1 = Comment.objects.filter(dis_id=prod).order_by('-date')
    return render(request,'forum/disc.html',{'data':data,'data1':data1})

def newdis(request):
    if request.user.is_authenticated:
        return render(request,'forum/new-dis.html')
    else:
        return redirect('/account/')
        
@login_required
def addnew(request):
    o = request.user
    data = {
        'topic' : request.POST.get('topic'),
        'content' : request.POST.get('content'),
        'name' : o.first_name,
        'last' : o.last_name,
    }
    nobj = Discussion.objects.create(**data)
    nobj.save()

    return redirect('/forum/')

def cmnt(request,prod):
    if request.user.is_authenticated:
        obj = Discussion.objects.get(pk=prod)
        return render(request,'forum/new-com.html',{'data':obj})
    else:
        return redirect('/account/')
@login_required
def addnewc(request,prod):
    o = request.user
    data = {
        'content' : request.POST.get('content'),
        'name' : o.first_name,
        'dis_id' : Discussion.objects.get(pk=prod),
    }
    nobj = Comment.objects.create(**data)
    nobj.save()
    obj = Discussion.objects.get(pk=prod)
    obj.cmnt += 1
    obj.save()
    return redirect('/forum/')
   

