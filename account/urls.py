from django.contrib.auth.decorators import login_required
from django.urls import include, path
from django.views.generic import TemplateView
from .views import GSTDocFileDownload, KYCDocFileDownload, Profile
from .views_account import (Confirmation, Forget, Login, Logout, Register,
                            send_login_otp, send_mobile_otp, verify_mobile_otp)
from .views_address import AddressDetail
from .views_bank import BankDetail
from .views_pickup import PickupDetail
from .views_company import CompanyDetail
from .views_entity import EntityDetail
from .views_general import GeneralDetail
from .views_gstin import GSTINDetail
from .views_representative import RepresentativeDetail

#accont related urls
urlpatterns=[
    path('',login_required(Profile),name='profile'),
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('forget/',Forget.as_view(),name='forget'),

# company related work here
    path('representativedetail/',login_required(RepresentativeDetail.as_view()),name='representativedetail'),
    path('companydetail/',login_required(CompanyDetail.as_view()),name='companydetail'),
    path('entitydetail/',login_required(EntityDetail.as_view()),name='entitydetail'),
    path('bankdetail/',login_required(BankDetail.as_view()),name='bankdetail'),
    path('pickupdetail/',login_required(PickupDetail.as_view())),
    path('addressdetail/',login_required(AddressDetail.as_view()),name='addressdetail'),
    path('confirmation/',Confirmation.as_view(),name='confirmation'),
    path('sendotplogin/',send_login_otp,name='sendotplogin'),
    path('sendmobileotp/',send_mobile_otp,name='sendmobileotp'),
    path('verifymobileotp/',verify_mobile_otp,name='verifymobileotp'),

    path('gstindetail/',GSTINDetail.as_view(),name='gstindetail'),
    path('generaldetail/',GeneralDetail.as_view(),name='generaldetail'),

    path('GSTdoc/<gstdoc>',GSTDocFileDownload,name='GSTdoc'),
    path('companyKYCdoc/<companykycdoc>',KYCDocFileDownload,name='companyKYCdoc')


]
