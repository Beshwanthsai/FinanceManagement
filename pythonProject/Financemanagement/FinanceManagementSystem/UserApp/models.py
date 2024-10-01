# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def create_random_categories():
        random_categories = ['Groceries', 'Travel', 'Education', 'Fitness', 'Gadgets']
        for category_name in random_categories:
            if not Category.objects.filter(name=category_name).exists():
                Category.objects.create(name=category_name)

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()