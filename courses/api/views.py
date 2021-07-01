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

from .serializers import *
from users.models import User
from courses.models import *



class AddCourseView(generics.CreateAPIView):
    serializer_class = AllCoursesSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        course_name = request.data.get("course_name")
        thumbnail = request.data.get("thumbnail")
        instructor_name = request.data.get("instructor_name")
        description = request.data.get("description")
        no_of_sections = request.data.get("no_of_sections")
        no_of_lectures = request.data.get("no_of_lectures")
        language = request.data.get("language")
        original_price = request.data.get("original_price")
        discount_percentage = request.data.get("discount_percentage")
        discounted_price = request.data.get("discounted_price")
        category = request.data.get("category")
        level = request.data.get("level")
        software = request.data.get("software")

        data = {
            "course_name": course_name,
            "thumbnail": thumbnail,
            "instructor_name": instructor_name,
            "description": description,
            "no_of_sections": no_of_sections,
            "no_of_lectures": no_of_lectures,
            "language": language,
            "original_price": original_price,
            "discount_percentage": discount_percentage,
            "discounted_price": discounted_price,
            "category": category,
            "level": level,
            "software": software,
        }

        serializer = AllCoursesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                "message": [
                    "Course has been added successfully"
                ]
                },
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CourseSectionView(generics.CreateAPIView):
    serializer_class = CourseSectionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        course = request.data.get("course")
        section_no = request.data.get("section_no")
        section_title = request.data.get("section_title")
        no_of_videos = request.data.get("no_of_videos")
        is_unlocked = request.data.get("is_unlocked")
        section_description = request.data.get("section_description")

        data = {
            "course": course,
            "section_no": section_no,
            "section_title": section_title,
            "no_of_videos": no_of_videos,
            "is_unlocked": is_unlocked,
            "section_description": section_description,
        }

        serializer = CourseSectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Section" + section_no + "has been added successfully to course: " + course
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


class LectureAddView(generics.CreateAPIView):
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        course_section = request.data.get("course_section")
        video_links = request.data.get("video_links")

        data = {
            "course_section": course_section,
            "video_links": video_links,
        }

        serializer = LectureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Lecture has been added successfully to section: " + course_section
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