from django.urls import path
from .import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.blog),
    path('Industry/', views.blog1),
    
    path('Ecommerce/', views.blog2),
    
    path('Seller-help/', views.blog3),
    
    path('Seller/', views.blog4),
    path('Learning/', views.blog5),
    path('Learning1/', views.blog6),
]
