from django.contrib import admin
from django.urls import path,include
from blog.api import views

urlpatterns = [
    path('blog/',views.blog_list),
    path('blog/<slug:slug>',views.blog_detail),
    path('tags/<slug:slug>',views.search_blog_by_tag),
]