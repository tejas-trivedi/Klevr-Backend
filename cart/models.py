from django.db import models
from users.models import User
from courses.models import AllCourses

class Cart(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(AllCourses, through='CartItem')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(AllCourses, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    line_item_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __int__(self):
        return str(self.id)