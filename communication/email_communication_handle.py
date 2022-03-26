from django.core.mail import send_mail
from django.template.loader import render_to_string
from theseventhsquare.settings import EMAILS


def account_register(intent,email,user,otp):
    html_message = render_to_string('email/register.html',{'otp':otp,'user':user})
    send_mail('Welcome to Seventh Square','',EMAILS['no_reply'],[email],fail_silently=False,html_message=html_message)
def account_forget(intent,email,user,otp):
    html_message = render_to_string('email/forget.html',{'otp':otp,'user':user})
    send_mail('Password reset OTP for Seventh Square','Please use OTP as a password your OTP is '+otp,EMAILS['no_reply'],[email],fail_silently=False)
    #send_mail('Password reset otp for seven square','',EMAILS['no_reply'],[email],fail_silently=False,html_message=html_message)
def account_sendOtpLogin(intent,email,user,otp):
    html_message = render_to_string('email/forget.html',{'otp':otp,'user':user})
    send_mail('Login OTP for Seventh Square','your login OTP is '+otp,EMAILS['no_reply'],[email],fail_silently=False)
    #send_mail('Password reset otp for seven square','',EMAILS['no_reply'],[email],fail_silently=False,html_message=html_message)
