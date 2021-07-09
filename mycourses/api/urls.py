from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('create/', CreateMyCoursesSection.as_view()),
    path('add/', AddCourseToMyCourses.as_view(), name="add_course_to_my_courses"),
    path('indexes/', MyCoursesListView.as_view(), name="my_courses_indexes_list"),
    path('list/', MyCoursesItemsListView.as_view(), name="my_courses_list"),
]

