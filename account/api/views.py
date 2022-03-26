from django.shortcuts import render
from django.http import HttpResponse,request,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from account.models import Account
from .serializers import AccountSerializer


@csrf_exempt
def companyname(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = Account.objects.get(id=pk)
    except Account.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AccountSerializer(product)
        return JsonResponse(serializer.data)

