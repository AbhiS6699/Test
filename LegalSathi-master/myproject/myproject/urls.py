# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


pages = {
    "partnership-deed": "partnership-deed.html",
    "index": "index.html",
    "base": "base.html",
    "enquiries": "enquiries.html",
    "add_partner": "add_partner.html",
    "anuual_compliance": "anuual_compliance.html",
    "food_license": "food_license.html",
    "legal_drafting": "legal_drafting.html",
    "llp_registration": "llp_registration.html",
    "noc": "noc.html",
    "partnership-deed": "partnership-deed.html",
    "pvt_ltd_registration": "pvt_ltd_registration.html",
    "remove_director": "remove_director.html",
    "rent_agreement": "rent_agreement.html",
    "section_8": "section_8.html",
    "dissolution_of_partnership": "dissolution_of_partnership.html",
    "gst_registration": "gst_registration.html",
    "gst_return_filing": "gst_return_filing.html",
    "itr_filing": "itr_filing.html",
    "tds_return_filing": "tds_return_filing.html",
    "pf_return_filing": "pf_return_filing.html",
    "trade_mark_registration": "trade_mark_registration.html",
    "GST_calculator": "GST_calculator.html",
    "EMI_calculator": "EMI_calculator.html",
    "sip_calculator": "sip_calculator.html",
    "FD_calculator": "FD_calculator.html",
    "80U_calculator": "80U_calculator.html",
    "HRA_calculator": "HRA_calculator.html",
    "TDS_caclulator": "TDS_caclulator.html",
    "simple_calculator": "simple_calculator.html",
    "test": "test.html"
    
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include the URLs from myapp
    path('', include('django.contrib.auth.urls')),  # for logout functionality

]
urlpatterns += [path(f'{name}/', TemplateView.as_view(template_name=template), name=name) for name, template in pages.items()]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

