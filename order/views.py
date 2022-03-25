from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def current(request):
    return render(request,'order/current.html')
def older(request):
    return render(request,'order/older.html')
