from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('create/', CreateMyCoursesSection.as_view()),
    path('add/', AddCourseToMyCourses.as_view(), name="add_course_to_my_courses"),
]

