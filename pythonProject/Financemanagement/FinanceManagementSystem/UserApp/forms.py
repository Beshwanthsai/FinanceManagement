# forms.py
from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('0-100', '0-100'),
        ('101-1000', '101-1000'),
        ('1001-10000', '1001-10000'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Expense
        fields = ['amount', 'category', 'date', 'description']