from django.urls import include, path
from rest_framework.routers import DefaultRouter as Router

from .views import NotificationViewSet

router = Router()
router.register('notification',NotificationViewSet,'notification')
urlpatterns=[
    path('',include(router.urls),name='notification'),
]
