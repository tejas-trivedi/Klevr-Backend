from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('my_cart/', MyCartListView.as_view(), name="my_cart"),
    path('items/', CartItemsListView.as_view(), name="items"),
    path('add_cart/', CreateMyCart.as_view(), name="create_cart"),
    path('add_item/', AddItemToCart.as_view(), name="add_item"),
    path('update/', UpdateMyCart.as_view(), name='update')
]
