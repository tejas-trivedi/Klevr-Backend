from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('wishlist/add/', AddCourseToWishlist.as_view(), name="add_to_wishlist"),
]

