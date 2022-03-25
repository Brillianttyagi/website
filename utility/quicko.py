#status_code
#404 gstin not found
#403 access denied; try  with otp
#400 invalid gstin number
#500 internal error
# 200 // ok
# 400 //bad request
# 404 //record not found
# 500 // internal error
# 403 //forbidden
# 401 // invalid token#401 

import datetime
import json
import logging
import time

import requests
from django.core.mail import mail_admins


def date_serialize(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

class Token:
    x_api_key = 'key_live_iGouNcOSsoyv6YdzN4mDxyOWZyjgiLHU'
    x_api_secret = 'secret_live_lx7vmRFqYfF7d4dIxi4OaIIE6Ri57s8d'
    x_api_version = '3.4.0'
    access_token = None
    
    def __init__(self,refresh=False):
        if refresh:
            self.authenticate()
            return
        try:
            json_file = open('quicko.txt')
            data = json.load(json_file)
            data['date'] = datetime.datetime.fromtimestamp(data['date'])
            date = data['date'] + datetime.timedelta(days=1)
            print(date,datetime.datetime.now())
            if date > datetime.datetime.now():
                self.access_token = data['access_token']
            else:
                self.access_token = data['access_token']
                self.authorize()
        except FileNotFoundError:        
            self.authenticate()
        except OSError:
            self.authenticate()

    def authenticate(self):
        url = "https://api.sandbox.co.in/authenticate"
        payload = {}
        headers = {
        'x-api-key':self.x_api_key ,
        'x-api-secret': self.x_api_secret ,
        'x-api-version':self.x_api_version 
        }
        response = requests.request("POST", url, headers=headers, data = payload)
        if response.status_code==200:
            data = json.loads(response.text.encode('utf8'))
            data['date'] = time.mktime(datetime.datetime.now().timetuple())
            print(data)
            with open('quicko.txt', 'w') as outfile:
                json.dump(data, outfile)
            print(data)
            self.access_token = data['access_token']
        else:
            log = logging.getLogger(__name__)
            mail_admins('quicko error','quicko authenticate : 403 Bad Credentials')
            log.error("quicko authenticate : 403 Bad Credentials")
            print('Bad Credentials')

    def authorize(self):
        url = "https://api.sandbox.co.in/authorize?request_token="+self.access_token
        payload = {}
        headers = {
        'Authorization': self.access_token,
        'x-api-key': self.x_api_key,
        'x-api-version': self.x_api_version
        }
        params = {
            "request_token" : self.access_token
        }
        response = requests.request("POST", url, headers=headers, data = payload,params=params)
        print(response.text)
        if response.status_code==200:
            data = json.loads(response.text.encode('utf8'))
            data['date'] = time.mktime(datetime.datetime.now().timetuple())
            with open('quicko.txt', 'w') as outfile:
                json.dump(data, outfile)
            self.access_token = data['access_token']
        else:
            self.access_token = None
            log = logging.getLogger(__name__)
            mail_admins('quicko error',"quicko authorize : 403 Bad Credentials")
            log.error("quicko authorize 403 Bad Credentials",)
            print('Bad Credentials')

class GSTIN:
    data = None
    status_code = None
    token = None
    logger = logging.getLogger(__name__)

    def __init__(self):
        token = Token()
        if token.access_token is not None:
            self.token = token

    def gstin(self,gstin):
        if gstin is not None:
            url = "https://api.sandbox.co.in/gsp/public/gstin/{}".format(gstin)
        else:
            self.status_code = 400 # bad request
            return

        payload = {}
        headers = {
        'Authorization': self.token.access_token,
        'x-api-key': self.token.x_api_key,
        'x-api-version': self.token.x_api_version
        }

        response = requests.request("GET", url, headers=headers, data = payload)
        if response.status_code==200:
            data = json.loads(response.text.encode('utf8'))
            if 'error_code' not in data:
                self.data = data
                self.status_code = 200
            else:
                if data['error_code']=='NOGSTIN':
                    self.status_code = 404 # record not found 
                elif data['error_code']=='SWEB_9035':
                    self.status_code = 400 #invalid gstin
                else:
                    data = response.text.encode('utf8')
                    print("Konown error")
                    self.logger.error("unknown error ,random code:567&&56fgf"+data)
        elif response.status_code==422:
            self.status_code=400 #invalid gstin
            data = response.text.encode('utf8')
            print("Invalid GSTIN pattern")
            self.logger.error("Invalid GSTIN pattern"+data)
        elif response.status_code==500:
            self.status_code = 500 #internal error
            data = response.text.encode('utf8')
            print("Internal Server Error")
            self.logger.error("Internal Server Error"+data)
        elif response.status_code == 403:
            data = json.loads(response.text.encode('utf8'))
            if data['message']=="Access denied":
                if gstin is not None:
                    self.status_code = 500 #forbidden
                else:
                    self.status_code = 500
            elif data['message']=="Invalid access token":
                token = Token(refresh=True)
                self.token = token
                self.status_code = 401
            elif data['message']=="Insufficient credits":
                self.status_code = 500
                mail_admins('quicko error','Insufficient credits')
                self.logger.error("Insufficient credits, code location : &kjdf7*&idhjd")
                print("Insufficient credits")
            else:
                self.status_code = 500
                self.logger.error('403 Forbidden :unknown error')
                
    
    
def gstin(gstin):
# 200 // ok
# 400 //bad request
# 404 //record not found
# 500 // internal error
# 403 //forbidden
# 401 // invalid token
    try:
        gstin = GSTIN()
        g=gstin.gstin(gstin=gstin)
        if g.status_code==401:
            t=Token(refresh=True)
            gstin = GSTIN()
            g=gstin.gstin(gstin=gstin)
        
        return{
            'status_code':g.status_code,
            'data':g.data
        }
    
    except Exception:
        return {
        'status_code' : 500,
        }


class Bank:
    data = None
    status_code = None
    token = None
    logger = logging.getLogger(__name__)

    def __init__(self):
        token = Token()
        if token.access_token is not None:
            self.token = token

    def bank(self,ifsc=None,account_number=None,name=None,mobile=None):
        if bank is not None and account_number is not None and name is not None and mobile is not None :
            url = "https://api.sandbox.co.in//bank/{ifsc}/accounts/{account_number}/verify?name={name}&mobile={mobile}".format(ifsc,account_number,name,mobile)
        else:
            self.status_code = 400 # bad request
            return

        payload = {}
        headers = {
        'Authorization': self.token.access_token,
        'x-api-key': self.token.x_api_key,
        'x-api-version': self.token.x_api_version
        }

        response = requests.request("GET", url, headers=headers, data = payload)
        if response.status_code==200:
            data = json.loads(response.text.encode('utf8'))
            if 'error_code' not in data:
                self.data = data
                self.status_code = 200
            else:
                if data['account_exists']:
                    self.status_code = 404 # record not found 
                else:
                    data = response.text.encode('utf8')
                    print("Konown error")
                    self.logger.error("unknown error ,random code:567&&56fgf"+data)
        elif response.status_code==422:
            self.status_code=400 #invalid gstin
            data = response.text.encode('utf8')
            print(response.message)
            self.logger.error("Invalid GSTIN pattern"+data)
        elif response.status_code==500:
            self.status_code = 500 #internal error
            data = response.text.encode('utf8')
            print("Internal Server Error")
            self.logger.error("Internal Server Error"+data)
        elif response.status_code == 403:
            data = json.loads(response.text.encode('utf8'))
            if data['message']=="Access denied":
                if bank is not None:
                    self.status_code = 500 #forbidden
                else:
                    self.status_code = 500
            elif data['message']=="Not a valid token":
                token = Token(refresh=True)
                self.token = token
                self.status_code = 401
            elif data['message']=="Insufficient credits":
                self.status_code = 500
                mail_admins('quicko error','Insufficient credits')
                self.logger.error("Insufficient credits, code location : &kjdf7*&idhjd")
                print("Insufficient credits")
            else:
                self.status_code = 500
                self.logger.error('403 Forbidden :unknown error')
                
    

def bank(self,ifsc,account_number,name,mobile):
# 200 // ok
# 400 //bad request
# 404 //record not found
# 500 // internal error
# 403 //forbidden
# 401 // invalid token
    try:
        bank = Bank()
        g=bank.bank(ifsc,account_number,name,mobile)
        if g.status_code==401:
            t=Token(refresh=True)
            bank = Bank()
            g=bank.bank(ifsc,account_number,name,mobile)
        
        return{
            'status_code':g.status_code,
            'data':g.data
        }
    

    except Exception:
        return {
        'status_code' : 500,
        'data':''
        }
