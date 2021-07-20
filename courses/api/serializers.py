from django.contrib.auth import authenticate, user_logged_in, user_login_failed
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group
from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.core.validators import EmailValidator

from users.models import User
from courses.models import *


class AllCoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AllCourses
        fields = ('id', 'course_name', 'thumbnail', 'instructor_name', 'description',
                'no_of_sections', 'no_of_lectures', 'language', 'original_price',
                'discount_percentage', 'discounted_price', 'category', 'level', 'software')

        def create(self, validated_data):
            course = AllCourses(
                course_name=validated_data["course_name"],
                thumbnail=validated_data["thumbnail"],
                instructor_name=validated_data["instructor_name"],
                description=validated_data["description"],
                no_of_sections=validated_data["no_of_sections"],
                no_of_lectures=validated_data["no_of_lectures"],
                language=validated_data["language"],
                original_price=validated_data["original_price"],
                discount_percentage=validated_data["discount_percentage"],
                discounted_price=validated_data["discounted_price"],
                category=validated_data["category"],
                level=validated_data["level"],
                software=validated_data["software"],
            )
            course.save()
            return course


class CourseSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseSection
        fields = ('course', 'section_no', 'section_title', 'no_of_videos',
                'is_unlocked', 'section_description', 'video_links')

        def create(self, validated_data):
            section = CourseSection(
                course=validated_data["course"],
                section_no=validated_data["section_no"],
                section_title=validated_data["section_title"],
                no_of_videos=validated_data["no_of_videos"],
                is_unlocked=validated_data["is_unlocked"],
                section_description=validated_data["section_description"],
                video_links=validated_data["video_links"],
            )
            section.save()
            return section

"""
class LectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = LectureVideos
        fields = ('course_section', 'video_links')

        def create(self, validated_data):
            lecture = CourseSection(
                course_section=validated_data["course_section"],
                video_links=validated_data["video_links"],
            )
            lecture.save()
            return lecture
"""