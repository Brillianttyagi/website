from background_task import background

from communication import email_communication_handle


@background(queue='email',schedule=1)
def send(intent,email,*args,**kwargs):
    if intent=='register':
        email_communication_handle.account_register(intent,email,*args,**kwargs)
    elif intent=='forget':
        email_communication_handle.account_forget(intent,email,*args,**kwargs)
    elif intent=='sendOtpLogin':
        email_communication_handle.account_sendOtpLogin(intent,email,*args,**kwargs)
