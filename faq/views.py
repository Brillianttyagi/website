from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Faq
from django.shortcuts import render, get_object_or_404
from taggit.models import Tag
# Create your views here.
def faq_view(request):
    info = Faq.objects.all()
    # print(popular_Faq)
    info = {
        'posts':info[0:10],
        
    }
    return render(request, 'dash-faqdashboard.html',info)
#Industry Faq home page
def post(request,slug):
    posts = Faq.objects.filter(tags=slug)
    
    context = {
        'tag':slug,
        'posts':posts,
    }
    return render(request, 'dash-faqaccount.html', context)