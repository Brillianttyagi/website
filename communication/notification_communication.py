from account.models import Account
from background_task import background

from .models import Notification


def send(request,intent,*args,**kwargs):
    if intent=='register':
        Notification.objects.create(account= Account.objects.get(pk=kwargs['user']),message="Welcome to Seventh Square")
