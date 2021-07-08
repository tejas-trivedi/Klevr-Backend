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
    #product = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = '__all__'

    #@staticmethod
    #def get_product(obj):
    #    return obj.product.name


class CartItemSerializer(serializers.ModelSerializer):
    #item = serializers.SerializerMethodField()
    #item_title = serializers.SerializerMethodField()
    #product = serializers.SerializerMethodField()
    #price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = [
            "cart",
            "item",
            #"item_title",
            #"price",
            #"product",
            "quantity",
            "line_item_total",
        ]


