from .email_communication import send as send_email
from .mobile_communication import send as send_mobile
from .notification_communication import send as send_notification


def send(request,intent,mobile=None,email=None,**kwargs):
    if intent in ['register','forget']:
        if mobile is not None:
            send_mobile(intent,mobile,user = kwargs['user'],otp=kwargs['otp'])
        if email is not None:
            send_email(intent,email,user = kwargs['user'],otp=kwargs['otp'])
        if email is not None or mobile is not None:
            send_notification(request,intent,**kwargs)
    elif intent =='sendOtpLogin':
        if mobile is not None:
            send_mobile(intent,mobile,user = kwargs['user'],otp=kwargs['otp'])
        if email is not None:
            send_email(intent,email,user = kwargs['user'],otp=kwargs['otp'])
    elif intent=='sendmobileotp':
        send_mobile(intent,mobile,otp=kwargs['otp'])
