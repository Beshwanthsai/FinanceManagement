from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0)

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField(default=timezone.now)