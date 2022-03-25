import logging

import requests


def twoFactorAuth(mobile,otp,template_name='OTP SMS'):
    api_key = 'd04e6b44-114b-11eb-9fa5-0200cd936042' 
    
    url = "https://2factor.in/API/V1/{}/SMS/{}/{}/{}".format(api_key,mobile,otp,template_name)
    res = requests.request('GET',url)
    if res.status_code==200:
        return 200
    else:
        logger = logging.getLogger(__name__)
        logger.error('twoFactorAuth 40 error')
        return 400
