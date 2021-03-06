from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import RegexValidator
from django.db import models
from courses.models import AllCourses


class UserManager(BaseUserManager):

    def create_user(self, email_id, password):

        if not email_id:
            raise ValueError("Email ID must be set")

        if not password:
            raise ValueError("Password must be set")
        # pass fields as arguments which are REQUIRED_FIELDS to user = self.model()
        user = self.model(email_id=email_id)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_id, password):
        # for super user admin role is fixed to 1
        user = self.create_user(email_id=email_id, password=password,)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    LANGUAGES = (
        ("NONE", "Choose a language"),
        ("ENGLISH", "English"),
        ("HINDI", "Hindi"),
        ("FRENCH", "French"),
        ("RUSSIAN", "Russian"),
    )

    email_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    headline = models.TextField(blank=True)
    language = models.CharField(max_length=25, choices=LANGUAGES, default="NONE")
    link = models.URLField()
    new_notif = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    is_staff = models.BooleanField(default=False, null=False, blank=False)
    is_superuser = models.BooleanField(default=False, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    # set USERNAME_FIELD to email_id
    USERNAME_FIELD = "email_id"
    # username AND password by default are included in REQUIRED_FIELDS
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __int__(self):
        return self.id

    def get_full_name(self):
        return f'{self.first_name} +" "+ {self.last_name}'



class Personalisation(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    design = models.BooleanField(default=False)
    programming = models.BooleanField(default=False)
    finance = models.BooleanField(default=False)
    marketing = models.BooleanField(default=False)
    music = models.BooleanField(default=False)
    writing = models.BooleanField(default=False)
    film = models.BooleanField(default=False)
    photography = models.BooleanField(default=False)

    def __str__(self):
        return f'User: {self.user}'



class Wishlist(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(AllCourses, through='WishlistItem')

    def __str__(self):
        return str(self.id)


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    item = models.ForeignKey(AllCourses, on_delete=models.CASCADE)

    def __int__(self):
        return self.wishlist.id