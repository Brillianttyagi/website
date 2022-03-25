from django.urls import path

from .views import reportandperformance

urlpatterns=[
    path('',reportandperformance,name='reportandperformance')
]
