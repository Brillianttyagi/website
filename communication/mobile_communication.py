from background_task import background

from . import mobile_communication_handle


@background(queue='mobile')
def send(intent,mobile,*args,**kwargs):
    print(__file__,__name__,__package__)
    if  intent=='register':
        mobile_communication_handle.account_register(intent,mobile,*args,**kwargs)
    elif intent=='forget':
        mobile_communication_handle.account_forget(intent,mobile,*args,**kwargs)
    elif intent=='sendOtpLogin':
        mobile_communication_handle.account_sendOtpLogin(intent,mobile,*args,**kwargs)
    elif intent=='sendmobileotp':
        mobile_communication_handle.account_sendMobileOtp(intent,mobile,*args,**kwargs)
