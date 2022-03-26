from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('',views.home),
    path('account/',include('account.urls')),
    path('enquiry/',include('enquiry.urls')),
    path('account/companyname/',include('account.api.urls')),
    path('inventory/',include('inventory.urls')),
    path('inventory/api/',include('inventory.api.urls')),
    path('communication/',include('communication.urls')),
    path('orders/',include('order.urls')),
    path('payments/',include('payment.urls')),
    path('customer-reviews/',include('customerview.urls')),
    path('reportandperformance/',include('reportandperformance.urls')),
    path('admin/', admin.site.urls),
    path('seller/', include('seller.urls')),

    path('notify_read/', views.notify_read),
    
    path('contact-us/', views.contact),
    path('find/', views.search ,name='search'),
    path('requestacallback/', views.requestacallback),
    path('callbackus/', views.callbackus),
    path('aftercontact/', views.aftercontact),
    path('partner/', views.partner),
    path('afterpartner/', views.afterpartner),
    path('corporate/', views.corporate),
    path('aftercorporate/', views.aftercorporate),
    path('careers/', views.careers),

    path('coming-soon/', views.coming),
    path('about/', views.about),
    path('commercial-terms/', views.comterm),
    path('guidelines/', views.selguide),
    path('policy/', views.policy),
    path('policy/returns/',TemplateView.as_view(template_name='dash-policyone.html')),
    path('policy/storage/',TemplateView.as_view(template_name='dash-policytwo.html')),
    path('policy/privacypolicy/',TemplateView.as_view(template_name='dash-privacypolicy.html')),
    path('marketplace/', views.marketplace),
    path('terms/', views.terms),

    path('docverify/',TemplateView.as_view(template_name='dash-docverify.html')),

    path('pricecalculator/', views.pricecalculator),
    path('preview/<str:prod>/', views.preview),

    path('blog/',include('blog.urls')),
    path('faq/',include('faq.urls')),
    path('forum/',include('forum.urls')),
    # path('<str:name>/',views.prod_view),

    path('how-it-works/',TemplateView.as_view(template_name='howitworks.html')),
    path('advertise-with-us/',TemplateView.as_view(template_name='advertisewithus.html')),
    path('pricing&commision/',TemplateView.as_view(template_name='pricing&commision.html')),
    path('previewFile/',TemplateView.as_view(template_name='preview.html')),
    path('sitemap/',TemplateView.as_view(template_name='sitemap.xml')),



]
if settings.DEBUG:
    
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
