# models.py
from django.db import models


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)  # Ensure this matches the form choices
    date = models.DateField()
    description = models.TextField()