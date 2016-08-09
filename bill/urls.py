from django.conf.urls import url, include
from views import BillViews, index

bill_list = BillViews.as_view({
    'get': 'list',
    'post': 'create'
})

bill_detail = BillViews.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
bill_payment = BillViews.as_view({
    'post': 'payment'
})
urlpatterns = [
    url(r'^$', index),
    url(r'(?P<ID>[0-9]+)/$', bill_detail,),
    url(r'(?P<ID>[0-9]+)/payment/$', bill_payment),
]