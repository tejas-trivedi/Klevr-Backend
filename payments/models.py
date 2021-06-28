from django.db import models
from users.models import User

# Create your models here.
class PaytmDataBase(models.Model):

    txn_user = models.CharField(max_length=100, null=True)
    order_id = models.CharField(max_length=150, unique=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    checksumhash = models.CharField(max_length=255)
    txn_id = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.order_id)