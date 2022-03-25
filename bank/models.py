from datetime import datetime

from account.models import Account
from django.db import models


class Bank(models.Model):
    STATUS_CHOICES=[
        ('YES','Yes'),
        ('NO','No'),
        ('Invalid','Invalid')
    ]
    BANK_CHOICES=[
        ('Airtel Payments Bank Ltd','Airtel Payments Bank Ltd'),
        ('American Express Banking Corp.','American Express Banking Corp.'),
        ('Au Small Finance Bank Ltd.','Au Small Finance Bank Ltd.'),
        ("Axis Bank Ltd.","Axis Bank Ltd."),
        ("Bandhan Bank Ltd.","Bandhan Bank Ltd."),
        ("Bank of Baroda","Bank of Baroda"),
        ("Bank of India","Bank of India"),
        ('Bank of Maharashtra','Bank of Maharashtra'),
        ('Barclays PLC','Barclays PLC'),
        ('BNP Paribas','BNP Paribas'),
        ('Canara Bank','Canara Bank'),
        ('Capital Small Finance Bank Ltd','Capital Small Finance Bank Ltd'),
        ('Central Bank of India','Central Bank of India'),
        ('CitiBank','CitiBank'),
        ('City Union Bank Ltd.','City Union Bank Ltd.'),
        ('Credit Suisse A.G','Credit Suisse A.G'),
        ('CSB Bank Limited','CSB Bank Limited'),
        ('DCB Bank Ltd.','DCB Bank Ltd.'),
        ('Deutsche Bank','Deutsche Bank'),
        ('Dhanlaxmi Bank Ltd.','Dhanlaxmi Bank Ltd.'),
        ('Equitas Small Finance Bank Ltd','Equitas Small Finance Bank Ltd'),
        ('ESAF Small Finance Bank Ltd.','ESAF Small Finance Bank Ltd.'),
        ('Federal Bank Ltd.','Federal Bank Ltd.'),
        ('Fincare Small Finance Bank Ltd.','Fincare Small Finance Bank Ltd.'),
        ('FINO Payments Bank Ltd','FINO Payments Bank Ltd'),
        ('HDFC Bank Ltd','HDFC Bank Ltd'),
        ('HSBC Ltd.','HSBC Ltd.'),
        ('ICICI Bank Ltd.','ICICI Bank Ltd.'),
        ('IDBI Bank Limited','IDBI Bank Limited'),
        ('IDFC FIRST Bank Limited','IDFC FIRST Bank Limited'),
        ('India Post Payments Bank Ltd','India Post Payments Bank Ltd'),
        ('Indian Bank','Indian Bank'),
        ('Indian Overseas Bank','Indian Overseas Bank'),
        ('IndusInd Bank Ltd','IndusInd Bank Ltd'),
        ('Jammu & Kashmir Bank Ltd.','Jammu & Kashmir Bank Ltd.'),
        ('Jana Small Finance Bank Ltd','Jana Small Finance Bank Ltd'),
        ('Jio Payments Bank Ltd','Jio Payments Bank Ltd'),
        ('Karnataka Bank Ltd.','Karnataka Bank Ltd.'),
        ('Karur Vysya Bank Ltd.','Karur Vysya Bank Ltd.'),
        ('Kotak Mahindra Bank Ltd','Kotak Mahindra Bank Ltd'),
        ('Lakshmi Vilas Bank Ltd.','Lakshmi Vilas Bank Ltd.'),
        ('Nainital bank Ltd.','Nainital bank Ltd.'),
        ('North East Small finance Bank Ltd','North East Small finance Bank Ltd'),
        ('NSDL Payments Bank Limited','NSDL Payments Bank Limited'),
        ('Paytm Payments Bank Ltd','Paytm Payments Bank Ltd'),
        ('Punjab & Sind Bank','Punjab & Sind Bank'),
        ('Punjab National Bank','Punjab National Bank'),
        ('RBL Bank Ltd.','RBL Bank Ltd.'),
        ('South Indian Bank Ltd.','South Indian Bank Ltd.'),
        ('Standard Chartered','Standard Chartered'),
        ('State Bank of India','State Bank of India'),
        ('Suryoday Small Finance Bank Ltd.','Suryoday Small Finance Bank Ltd.'),
        ('Tamilnad Mercantile Bank Ltd.','Tamilnad Mercantile Bank Ltd.'),
        ('UCO Bank','UCO Bank'),
        ('Ujjivan Small Finance Bank Ltd.','Ujjivan Small Finance Bank Ltd.'),
        ('Union Bank of India','Union Bank of India'),
        ('Utkarsh Small Finance Bank Ltd.','Utkarsh Small Finance Bank Ltd.'),
        ('YES Bank Ltd','YES Bank Ltd')
    ]

    account = models.ForeignKey(Account,on_delete=models.SET_NULL, null=True,blank=True)
    accountHolderName = models.CharField(max_length=30)
    accountNumber = models.CharField(max_length=30,unique=True)
    ifsc = models.CharField(max_length=30)
    bank = models.CharField(max_length=40,choices=BANK_CHOICES)
    branch = models.CharField(max_length=40)
    isVerified = models.CharField(max_length=10,choices=STATUS_CHOICES,default='NO')
    date = models.DateTimeField(default=datetime.now)
    mobile = models.CharField(max_length=13,default='')

    def __str__(self):
        return self.accountHolderName
