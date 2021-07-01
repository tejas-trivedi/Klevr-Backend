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
from decimal import Decimal


from .serializers import *
from users.models import User
from cart.models import *


class MyCartListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        try:
            cart = Cart.objects.filter(user=request.user)
            print(cart)
            context = {
                "request": request,
            }

            my_cart_serializer = CartSerializer(cart, many=True, context=context)
            response = my_cart_serializer.data


            cart_item = CartItem.objects.filter(cart=cart[0])

            my_cart = Cart()
            total_cart_amount = 0
            cart_item_serializer = CartItemSerializer(cart_item, many=True, context=context)
            response_temp = cart_item_serializer.data

            for res in range(0, len(response_temp)):
                total_cart_amount += Decimal(response_temp[res]['line_item_total'])

            my_cart.total = total_cart_amount
            print(my_cart.total)
            #my_cart.save()

            return Response(response, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            errors = {"message":["No cart found"]}
            return Response(errors, status=status.HTTP_404_NOT_FOUND)



class CartItemsListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        try:
            cart = Cart.objects.filter(user=request.user)

            cart1 = cart.values_list('id', flat=True)
            cart_item = CartItem.objects.filter(cart=cart[0])

            context = {
                "request": request,
            }

            cart_item_serializer = CartItemSerializer(cart_item, many=True, context=context)
            response = cart_item_serializer.data

            total_cart_amount = 0

            for res in range(0, len(response)):
                total_cart_amount += Decimal(response[res]['line_item_total'])

            return Response(response, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            errors = {"message":["No cart found"]}
            return Response(errors, status=status.HTTP_404_NOT_FOUND)



class CreateMyCart(APIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        #items = request.data.get("items")

        data = {
            "user": request.user,
            #"items": items,
        }

        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Your cart is ready"
            }
            return Response(
                response,
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class AddItemToCart(APIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        my_cart = Cart.objects.filter(user=request.user)


        cart = my_cart[0]
        item = request.data.get("item")
        quantity = request.data.get("quantity")

        data = {
            "cart": cart,
            "item": item,
            "quantity": quantity
        }

        serializer = CartItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Item has been added to the cart of user: "+ cart.user
            }
            return Response(
                response,
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )