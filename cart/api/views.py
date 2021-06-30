from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, mixins, serializers, status
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404


from .serializers import *
from users.models import User
from cart.models import *


class MyCartListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        try:
            cart = Cart.objects.filter(user=request.user)
            context = {
                "request": request,
            }

            my_cart_serializer = CartSerializer(cart, many=True, context=context)
            response = my_cart_serializer.data
            return Response(response, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            errors = {"message":["No cart found"]}
            return Response(errors, status=status.HTTP_404_NOT_FOUND)



class CartItemsListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        try:
            #cart1 = Cart.objects.filter(user=request.user)
            cart1 = get_object_or_404(Cart, user=request.user)
            print(cart1)
            cart_item = CartItem.objects.filter(cart=cart1.items.all())
            context = {
                "request": request,
            }

            cart_item_serializer = CartItemSerializer(cart_item, many=True, context=context)
            response = cart_item_serializer.data
            return Response(response, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            errors = {"message":["No cart found"]}
            return Response(errors, status=status.HTTP_404_NOT_FOUND)

