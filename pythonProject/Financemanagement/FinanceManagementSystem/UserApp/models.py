# models.py
from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Balance(models.Model):
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.initial_balance)