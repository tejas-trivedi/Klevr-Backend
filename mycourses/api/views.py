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
import cv2
import datetime

from .serializers import *
from cart.models import *
from users.models import User
from courses.models import *
from courses.api.serializers import AllCoursesSerializer, CourseSectionSerializer


class MyCoursesListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        try:
            courses = MyCourses.objects.filter(user=request.user)
            context = {
                "request": request,
            }

            my_courses_serializer = MyCoursesSerializers(courses, many=True, context=context)
            response = my_courses_serializer.data

            return Response(response, status=status.HTTP_200_OK)

        except MyCourses.DoesNotExist:
            errors = {"message":["You dont have any courses section"]}
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
                status = status.HTTP_201_CREATED
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


        data = {
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
                status = status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )



class MyCoursesItemsListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        try:
            my_course = MyCourses.objects.filter(user=request.user)

            mycourses1 = my_course.values_list('courses', flat=True)
            print(len(mycourses1))

            my_courses_list = []

            for i in range(0, len(mycourses1)):
                course = AllCourses.objects.filter(id=str(mycourses1[i]))
                all_serializer = AllCoursesSerializer(course, many=True,)
                #print(all_serializer.data)
                data_tba = all_serializer.data
                my_courses_list.append(data_tba)

            print(my_courses_list)
            response = my_courses_list

            context = {
                "request": request,
            }

            return Response(response, status=status.HTTP_200_OK)

        except MyCourses.DoesNotExist:
            errors = {"message":["You haven't purchased any course yet"]}
            return Response(errors, status=status.HTTP_404_NOT_FOUND)




class MyCourseDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        this_course = get_object_or_404(AllCourses, id=pk)

        #section = get_object_or_404(CourseSection, course=this_course.id)
        section = CourseSection.objects.filter(course=this_course)


        all_sections_data = []
        durations = []
        #total_response = []

        for i in range(0, len(section)):
            section_serializer = CourseSectionSerializer(section[i])
            videos = section_serializer.data['video_links']

            """for i in range(1, len(videos)+1):

                data = cv2.VideoCapture(videos[str(i)])
                frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
                fps = int(data.get(cv2.CAP_PROP_FPS))

                seconds = int(frames / fps)
                video_time = str(datetime.timedelta(seconds=seconds))
                print("duration in seconds:", seconds)
                print("video time:", video_time)

                durations.append(video_time)"""

            all_sections_data.append(section_serializer.data)

            #serializer5 = all_sections_data + durations
            #total_response.append(serializer5)

        response = {
            "all_sections": all_sections_data,
            #"duration": durations
        }

        return Response(response, status=status.HTTP_200_OK)



class MyReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        course_id = request.data.get("course")
        review = request.data.get("review")

        data = {
            "user": request.user,
            "course": course_id,
            "review": review,
        }

        serializer = MyReviewSerializer(data=data)
        if serializer.is_valid():
            print("Yes")
            serializer.save()
            response = {
                "message": "Your review has been posted successfully"
            }

            return Response(
                response,
                status = status.HTTP_200_OK
            )

        else:
            return Response(
                {
                    "message": "Something went wrong!"
                },
                status = status.HTTP_400_BAD_REQUEST,
            )


class AllReviewOnCourseView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        course_id = self.request.query_params.get("course_id")
        course = MyReview.objects.filter(course = course_id)
        print(course)

        reviews_list = []

        for i in range(0, len(course)):
            serializer = MyReviewSerializer(course[i])
            reviews_list.append(serializer.data)

        print(reviews_list)

        response = {
            "all_reviews": reviews_list,
        }

        return Response(response, status=status.HTTP_200_OK)

