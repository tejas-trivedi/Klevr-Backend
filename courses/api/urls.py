from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('add/course/', AddCourseView.as_view(), name="add_course"),
    path('add/section/', CourseSectionView.as_view(), name="add_section"),
    path('add/lecture/', LectureAddView.as_view(), name="add_section"),
    path('all/', AllCoursesListView.as_view(), name="all_courses_list"),
    path('programming/', ProgrammingCoursesListView.as_view(), name='programming_courses_list'),
    path('design/', DesignCoursesListView.as_view(), name='design_courses_list'),
    path('finance/', FinanceCoursesListView.as_view(), name='finance_courses_list'),
    path('marketing/', MarketingCoursesListView.as_view(), name='marketing_courses_list'),
    path('music/', MusicCoursesListView.as_view(), name='music_courses_list'),
    path('writing/', WritingCoursesListView.as_view(), name='writing_courses_list'),
    path('film/', FilmCoursesListView.as_view(), name='film_courses_list'),
    path('photography/', PhotographyCoursesListView.as_view(), name='photography_courses_list'),
]

