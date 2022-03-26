from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,request,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from inventory.models import Inventory,PostPicture,ServiceRegionOfSeller
from .serializers import BlogSerializer,ImageSerializer,ServiceSerializer
from taggit.models import Tag

@csrf_exempt
def inventory_list(request):
    if request.method == 'GET':
        blogs = Inventory.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def inventory_detail_by_id(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = Inventory.objects.get(id=pk)
    except Inventory.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogSerializer(product)
        return JsonResponse(serializer.data)

@csrf_exempt
def inventory_detail_by_category(request, cat):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = Inventory.objects.filter(subCategory=cat)
    except Inventory.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogSerializer(product,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def getpic(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    print(pk)
    try:
        product = PostPicture.objects.filter(postid=pk)
    except Inventory.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ImageSerializer(product,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def inventory_detail_by_location(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = Inventory.objects.filter(servicedRegions=pk)
    except Inventory.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogSerializer(product,many = True)
        return JsonResponse(serializer.data,safe = False)

@csrf_exempt
def inventory_detail_by_tags(request, pk,sr):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        tag = pk.split("_")
        product = Inventory.objects.filter(product_tags__name__in=tag,servicedRegions=sr).distinct()
    except Inventory.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogSerializer(product,many = True)
        return JsonResponse(serializer.data,safe = False)

@csrf_exempt
def getregions(request, pk,city):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = ServiceRegionOfSeller.objects.filter(account=pk,region=city)
    except Inventory.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ServiceSerializer(product,many=True)
        return JsonResponse(serializer.data,safe=False)