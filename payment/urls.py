from django.urls import include, path

from .views import payment

urlpatterns=[
    path('',payment,name='payment')
]
