from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('details',views.quotation),
    path('reply',views.reply),
    path('proposal',views.proposal),
    path('proposalreply',views.proposalreply),
    path('information',views.information),
    path('informationreply',views.informationreply),
    path('bpo',views.bpo),
    path('bporeply',views.bporeply),
    path('admin_main_enquiry',views.admin_main),
    path('admin_reply',views.admin_main_reply),

]