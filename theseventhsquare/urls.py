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
    path('inventory/',include('inventory.urls')),
    path('communication/',include('communication.urls')),
    path('orders/',include('order.urls')),
    path('payments/',include('payment.urls')),
    path('customer-reviews/',include('customerview.urls')),
    path('reportandperformance/',include('reportandperformance.urls')),
    path('admin/', admin.site.urls),
    path('seller/', include('seller.urls')),

    path('notify_read/', views.notify_read),
    
    path('contact-us/', views.contact),
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
    path('marketplace/', views.marketplace),
    path('terms/', views.terms),
    path('faq/',TemplateView.as_view(template_name='dash-faqaccount.html')),
    path('docverify/',TemplateView.as_view(template_name='dash-docverify.html')),
    path('faqs/<str:f>/', views.dash_faqs),
    path('pricecalculator/', views.pricecalculator),
    path('preview/<str:prod>/', views.preview),

    path('blog/',include('blog.urls')),
    path('forum/',include('forum.urls')),
    # path('<str:name>/',views.prod_view),
    path('how-it-works/',TemplateView.as_view(template_name='howitworks.html')),
    path('advertise-with-us/',TemplateView.as_view(template_name='advertisewithus.html')),
    path('pricing&commision/',TemplateView.as_view(template_name='pricing&commision.html')),
    path('serviced/',TemplateView.as_view(template_name='servicedRegion.html')),
    path('sitemap/',TemplateView.as_view(template_name='sitemap.xml')),

    # blogs links starting from herein
    path('Industry/Furniture_E-commerce_in_India/',TemplateView.as_view(template_name='Industry1.html')),
    path('Industry/Trends_in_the_Building_Materials_Industry/',TemplateView.as_view(template_name='Industry2.html')),
    path('Industry/How_Cement_Manufacturers_can_grow_by_selling_online/',TemplateView.as_view(template_name='Industry3.html')),
    path('Industry/Construction_Steel_market_in_India_and_Emerging_Trends/',TemplateView.as_view(template_name='Industry4.html')),
    path('Industry/Green_Buildings_India_Build_back_better/',TemplateView.as_view(template_name='Industry5.html')),
    path('ecommerce/How_e-commerce_can_help_you_grow/',TemplateView.as_view(template_name='ecommerce1.html')),
    path('ecommerce/Tips_&_Tricks_For_Selling_Online/',TemplateView.as_view(template_name='ecommerce2.html')),
    path('ecommerce/Importance_of_Packaging_in_E-commerce/',TemplateView.as_view(template_name='ecommerce3.html')),
    path('ecommerce/Why_online_marketplaces_work/',TemplateView.as_view(template_name='ecommerce4.html')),
    path('ecommerce/Sell_online_to_build_Brand_Awareness/',TemplateView.as_view(template_name='ecommerce5.html')),
    path('ecommerce/How_Seventh_Square_helps_you_in_selling_Building_aterials_to_Businesses/',TemplateView.as_view(template_name='ecommerce6.html')),
    path('seller-help/Seventh_Square_Business/',TemplateView.as_view(template_name='sellerhelp1.html')),
    path('seller-help/Seventh_Square_Seller/',TemplateView.as_view(template_name='sellerhelp2.html')),
    path('seller-help/write_Product_Title_and_Product_Description/',TemplateView.as_view(template_name='sellerhelp3.html')),
    path('seller-help/HSN_Code_&_Ecommerce/',TemplateView.as_view(template_name='sellerhelp4.html')),
    path('seller-help/Adding_new_product_Serviced_Regions/',TemplateView.as_view(template_name='sellerhelp5.html')),
    path('seller-help/What_is_RFX_How_does_it_help_me/',TemplateView.as_view(template_name='sellerhelp6.html')),
    path('previewact/',TemplateView.as_view(template_name='previewact.html')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
