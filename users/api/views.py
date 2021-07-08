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

        #wish = Wishlist.objects.filter(user=request.user)

        course_id = request.data.get("course_id")

        wishlist_course = AllCourses.objects.filter(id=course_id)
        print(wishlist_course[0])

        data = {
            "user": request.user,
            "wishlist": wishlist_course[0],
        }

        serializer = WishlistSerializer(data=data, partial=True)
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