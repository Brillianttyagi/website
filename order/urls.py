from django.urls import include, path

from .views import current, older

urlpatterns=[
    path('current-orders/',current,name='ordercurrent'),
    path('past-orders/',older,name='orderolder')
    
]
