from django.urls import path
from .views import *

urlpatterns = [
    #path('', views.index, name='index'),
    path('',PaytmRequest.as_view()),
    path('test/', TestPaytm.as_view()),
    path('payment_response/', PaytmResponse.as_view()),
    path('status/', paytm_transection_status),
]