from django.db import models
from django.utils import timezone

class Balance(models.Model):
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2)

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)