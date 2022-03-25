from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,request,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from blog.models import Blog
from .serializers import BlogSerializer,TagSerializer,MainSerializer
from taggit.models import Tag
from hitcount.views import HitCountDetailView
from collections import namedtuple


@csrf_exempt
def blog_list(request):
    if request.method == 'GET':
        Main = namedtuple('blog', ('posts', 'tags'))
        data = Main(
            posts = Blog.objects.all(),
            tags = Blog.tags.most_common()[:18]
        )
        
        serializer = MainSerializer(data)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def blog_detail(request, slug):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        blogs = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogSerializer(blogs)
        return JsonResponse(serializer.data)

@csrf_exempt
def popular_blog_detail(request):
    '''
    Return top 6 Popular blogs
    '''
    try:
        popular_blog = Blog.objects.order_by('hit_count_generic')[:6]
    except:
        return HttpResponse(status= 404)
    if request.method == 'GET':
        serializer = BlogSerializer(popular_blog,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def search_blog_by_tag(request,slug):
    '''
    Return all blog post of an specific tag
    '''
    try:
        tag = get_object_or_404(Tag, slug=slug)
        posts = Blog.objects.filter(tags=tag)
    except:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = BlogSerializer(posts,many = True)
        return JsonResponse(serializer.data,safe = False)


    