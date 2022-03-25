from django.shortcuts import render


# Create your views here.
def customerview(request):
    return render(request,'customerview/customerview.html')
