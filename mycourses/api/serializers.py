from django.contrib.auth import authenticate, user_logged_in, user_login_failed
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group
from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.core.validators import EmailValidator

from users.models import User
from mycourses.models import *



class MyCoursesSerializers(serializers.ModelSerializer):

    class Meta:
        model = MyCourses
        fields = [
            "user",
            "courses",
        ]


class MyReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyReview
        fields = [
            "user",
            "course",
            "review"
        ]

"""class MyCoursesItemsSerializers(serializers.ModelSerializer):

    class Meta:
        model = MyCoursesItems
        fields = [
            "my_course",
            "course",
        ]"""