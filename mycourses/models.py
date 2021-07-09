from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from courses.models import AllCourses
from users.models import User


class MyCourses(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(AllCourses, blank=True)

    def __str__(self):
        return str(self.id)


"""
class MyCoursesItems(models.Model):

    my_course = models.ForeignKey(MyCourses, on_delete=models.CASCADE)
    course = models.ForeignKey(AllCourses, on_delete=models.CASCADE)

    def __int__(self):
        return str(self.id)
"""

