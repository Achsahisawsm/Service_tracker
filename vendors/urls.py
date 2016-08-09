
from django.conf.urls import url
from .views import index,VendorViewSet

vendor_list = VendorViewSet.as_view({'get': 'list','post':'create'})
vendor_detail = VendorViewSet.as_view({'get': 'retrieve', 'put':'update','delete':'destroy'})
urlpatterns = [

   url(r'^$',vendor_list),
   url(r'(?P<ID>[0-9]+)',vendor_detail),



]