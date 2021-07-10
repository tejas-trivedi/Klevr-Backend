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



class MyWishListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        try:
            cart = Wishlist.objects.filter(user=request.user)
            print(cart)
            context = {
                "request": request,
            }


            my_wish_serializer = WishlistSerializer(cart, many=True, context=context)
            response = my_wish_serializer.data


            wish_item = WishlistItem.objects.filter(wishlist=cart[0])
            wish_item_serializer = WishlistItemSerializer(wish_item, many=True, context=context)
            response_temp = wish_item_serializer.data


            return Response(response, status=status.HTTP_200_OK)

        except Wishlist.DoesNotExist:
            errors = {"message":["No Wishlist found"]}
            return Response(errors, status=status.HTTP_404_NOT_FOUND)




class CreateMyWishlist(APIView):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        data = {
            "user": request.user,
        }
        serializer = WishlistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Your wishlist is ready"
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



class AddItemToWishlist(APIView):
    serializer_class = WishlistItemSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        my_wish = Wishlist.objects.filter(user=request.user)

        wish = my_wish[0]
        print(wish)
        #print(cart)
        item = request.data.get("item")

        data = {
            "wishlist": str(wish),
            "item": item,
        }

        serializer = WishlistItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Item has been added to the wishlist"
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



class WishlistItemsListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        try:
            wish = Wishlist.objects.filter(user=request.user)

            wish1 = wish.values_list('items', flat=True)
            print(len(wish1))
            wish_item = WishlistItem.objects.filter(wishlist=wish[0])
            #print(cart_item)

            my_wish_courses_list = []

            for i in range(0, len(wish1)):
                course = AllCourses.objects.filter(id=str(wish1[i]))
                all_serializer = AllCoursesSerializer(course, many=True,)
                #print(all_serializer.data)
                data_tba = all_serializer.data
                my_wish_courses_list.append(data_tba)

            print(my_wish_courses_list)
            response = my_wish_courses_list

            context = {
                "request": request,
            }

            return Response(response, status=status.HTTP_200_OK)

        except Cart.DoesNotExist:
            errors = {"message":["No cart found"]}
            return Response(errors, status=status.HTTP_404_NOT_FOUND)
