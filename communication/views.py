from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Notification


class CSRF_EXEMPT_SessionAuthentication(SessionAuthentication):
    def enforce_csrf(self,request):
        pass

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id','account','message','isReaded']

class NotificationViewSet(ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [CSRF_EXEMPT_SessionAuthentication]
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size= 5

    def get_queryset(self):
        return Notification.objects.filter(account=self.request.user)

    @action(methods=['post'],detail=True)
    @csrf_exempt
    def markasread(self,request,pk):
        try:
            notification= Notification.objects.get(pk=pk)
            notification.isReaded=True
            notification.save()
            return Response({'id':notification.pk,'detail':'marked as readed'})
        except ObjectDoesNotExist:
            return Response({'id':pk,'detail':'fail'},status=404)
    @action(methods=['post'],detail=False)
    def markallasread(self,request):
        try:
            notification= Notification.objects.filter(account=request.user)
            notification.update(isReaded=True)
            return Response({'detail':'marked as readed'})
        except ObjectDoesNotExist:
            return Response({'detail':'fail'},status=404)
