from background_task import background
from utility.quicko import gstin,bank
from account.models import Account
from logging import getLogger

from bank.models import Bank

@background(queue='gstin',schedule=1)
def fetch_gstin_detail(gstin_number,user_id,**kwarg):
    res = gstin(gstin=gstin_number)
    try:
        account = Account.object.get(pk=user_id)
        account.gstin_data_status = res.status_code
        account.gstin_data = res.get('data','')
        account.save()
    except Exception:
        log = getLogger(__name__)
        log.error('GST Data Fetching Fail')
        print('GST Data Fetching Fail')

@background(queue='bank',schedule=1)
def fetch_bank_detail(ifsc,account_number,name,mobile,user_id,**kwarg):
    res = bank(gstin=gstin_number)
    try:
        account = Account.object.get(pk=user_id)
        account.gstin_data_status = res.status_code
        account.gstin_data = res.get('data','')
        account.gstin_data_status = res.status_code
        account.gstin_data = res.data
        account.save()
    except Exception:
        log = getLogger(__name__)
        log.error('Bank Data Fetching Fail')
        