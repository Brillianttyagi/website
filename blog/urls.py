from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog),
    path('tag/<slug:slug>/', views.post, name="post"),
    
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('add_post', views.addblog , name='add_post'),
    path('Ecommerce/', views.blog2),
    
    path('Seller-help/', views.blog3),
    
    path('Seller/', views.blog4),
    path('Learning/', views.blog5),
    path('Learning1/', views.blog6),
]

