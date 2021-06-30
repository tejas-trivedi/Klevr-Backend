from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('my_cart/', MyCartListView.as_view(), name="my_cart"),
    path('items/', CartItemsListView.as_view(), name="items"),
]
