from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('wishlist/view/', MyWishListView.as_view(), name="my_wishlist"),
    #path('items/', CartItemsListView.as_view(), name="items"),
    path('wishlist/add/', CreateMyWishlist.as_view(), name="create_wishlist"),
    path('wishlist/add_item/', AddItemToWishlist.as_view(), name="add_item"),
    #path('wishlist/update/', UpdateMyWishlist.as_view(), name='update')
]
