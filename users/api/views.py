from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.utils import timezone
from django.db import models
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
from courses.api.serializers import AllCoursesSerializer



class AddCourseToWishlist(APIView):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        wish = Wishlist.objects.filter(user=request.user)

        course_id = list(request.data.get("course_id"))

        #wishlist_course = list(AllCourses.objects.filter(id=course_id))
        #print(wishlist_course)

        data = {
            "user": request.user,
            "wishlist": course_id,
        }

        serializer = WishlistSerializer(wish[0], data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Item has been added to the Wishlist"
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


"""
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


class UpdateMyCart(APIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        cart = Cart.objects.filter(user=request.user)
        context = {
                "request": request,
            }
        cart_item = CartItem.objects.filter(cart=cart[0])

        #my_cart = Cart()
        total_cart_amount = 0
        cart_item_serializer = CartItemSerializer(cart_item, many=True, context=context)
        response_temp = cart_item_serializer.data

        for res in range(0, len(response_temp)):
            total_cart_amount += Decimal(response_temp[res]['line_item_total'])

        print(total_cart_amount)

        data = {
            "total": total_cart_amount,
        }
        serializer = CartSerializer(cart[0], data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Your cart is updated"
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
        #print(cart)
        item = request.data.get("item")
        quantity = request.data.get("quantity")

        item_course = AllCourses.objects.filter(id=item)
        #item_price = item_course.discounted_price
        item_price = Decimal(list(item_course.values_list('discounted_price', flat=True))[0])
        print(item_price)

        data = {
            "cart": str(cart),
            "item": item,
            "quantity": quantity,
            "line_item_total": item_price*int(quantity),
        }

        serializer = CartItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Item has been added to the cart"
            }

            return Response(
                response,
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )"""