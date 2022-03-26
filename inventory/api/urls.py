from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.inventory_list),
    path('inventory_detail/<int:pk>',views.inventory_detail_by_id),
    path('inventory_detail/location/<slug:pk>',views.inventory_detail_by_id),
    path('inventory_detail_by_category/<str:cat>',views.inventory_detail_by_category),
    path('inventory_detail_by_location/<str:pk>',views.inventory_detail_by_location),
    path('inventory_detail_by_tags/<str:sr>/<str:pk>',views.inventory_detail_by_tags),
    path('picture/<int:pk>',views.getpic),
    path('service/<int:pk>/<str:city>',views.getregions),
]