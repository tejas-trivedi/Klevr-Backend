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
from cart.models import *
from users.models import User
from courses.api.serializers import AllCoursesSerializer



class MyCoursesListView(APIView):

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




class CreateMyCoursesSection(APIView):
    serializer_class = MyCoursesSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        data = {
            "user": request.user,
        }
        serializer = MyCoursesSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "My courses section is ready"
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



class AddCourseToMyCourses(APIView):
    serializer_class = MyCoursesSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        my_courses_section = MyCourses.objects.filter(user=request.user)
        my_cart = Cart.objects.filter(user=request.user)

        my_cart_items = list(my_cart.values_list('items', flat=True))
        print(my_cart_items)

        course = my_courses_section[0]
        print(course)
        #print(cart)
        #item = request.data.get("item")

        data = {
            #"wishlist": str(wish),
            "user": request.user,
            "courses": my_cart_items,
        }

        serializer = MyCoursesSerializers(course, data=data, partial=True)
        if serializer.is_valid():
            print("Yess")
            serializer.save()
            response = {
                "message": "Item/Items have been added to the my courses"
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
class AddCourseToMyCourses(APIView):
    serializer_class = MyCoursesItems
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        my_cart = Cart.objects.filter(user=request.user)
        my_courses_section = MyCourses.objects.filter(user=request.user)
        print(my_courses_section[0])
        print(len(my_cart))

        for i in range(0, len(my_cart)):

            course = list(my_cart.values_list('items', flat=True))[i]
            print(course)

            data = {
                "my_course": str(my_courses_section[0]),
                "course": course,
            }

            serializer = MyCoursesItemsSerializers(data=data)
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
                )
"""


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
