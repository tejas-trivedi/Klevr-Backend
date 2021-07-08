from django.contrib.auth import authenticate, user_logged_in, user_login_failed
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group
from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.core.validators import EmailValidator

from users.models import User
from cart.models import *


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'

    #@staticmethod
    #def get_product(obj):
    #    return obj.product.name


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = [
            "cart",
            "item",
            "quantity",
            "line_item_total",
        ]


