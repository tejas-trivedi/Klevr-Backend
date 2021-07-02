from django.db import models
from users.models import User
import jsonfield


class AllCourses(models.Model):

    LANGUAGES = (
        ("NONE", "Choose a language"),
        ("ENGLISH", "English"),
        ("HINDI", "Hindi"),
        ("FRENCH", "French"),
        ("RUSSIAN", "Russian"),
    )

    RATINGS = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    CATEGORIES = (
        ("NONE", "None"),
        ("DESIGN", "Design"),
        ("PROGRAMMING", "Programming"),
        ("FINANCE", "Finance"),
        ("MARKETING", "Marketing"),
        ("MUSIC", "Music"),
        ("WRITING", "Writing"),
        ("FILM", "Film"),
        ("PHOTOGRAPHY", "Photography")
    )

    LEVELS = (
        ("NONE", "None"),
        ("BEGINNER", "Beginner"),
        ("INTERMEDIATE", "Intermediate"),
        ("ADVANCED", "Advanced"),
    )

    course_name = models.CharField(max_length=150)
    thumbnail = models.URLField()
    instructor_name = models.CharField(max_length=25)
    description = models.TextField()
    no_of_sections = models.PositiveIntegerField()
    no_of_lectures = models.PositiveIntegerField()
    total_length = models.DurationField(default=0)
    language = models.CharField(max_length=25, choices=LANGUAGES, default="NONE")
    original_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    rating = models.PositiveIntegerField(choices=RATINGS, default=0)
    category = models.CharField(max_length=25, choices=CATEGORIES, default="NONE")
    level = models.CharField(max_length=25, choices=LEVELS, default="NONE")
    software = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name



class CourseSection(models.Model):

    course = models.ForeignKey(AllCourses, on_delete=models.CASCADE)
    section_no = models.PositiveIntegerField()
    section_title = models.CharField(max_length=50)
    no_of_videos = models.PositiveIntegerField()
    is_unlocked = models.BooleanField(default=False)
    section_description = models.TextField()

    def __str__(self):
        return self.section_title


class LectureVideos(models.Model):

    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    video_links = jsonfield.JSONField()

    def __int__(self):
        return self.id



