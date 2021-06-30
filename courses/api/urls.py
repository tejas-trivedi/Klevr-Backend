from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('add/course/', AddCourseView.as_view(), name="add_course"),
    path('add/section/', CourseSectionView.as_view(), name="add_section"),
    path('add/lecture/', LectureAddView.as_view(), name="add_section"),
]
