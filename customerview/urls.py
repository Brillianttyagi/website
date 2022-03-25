from django.urls import include, path

from .views import customerview

urlpatterns =[
    path('',customerview,name='customerview')
]
