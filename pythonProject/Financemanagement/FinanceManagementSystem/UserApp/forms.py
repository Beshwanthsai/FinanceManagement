from django import forms
from .models import Expense, UserBalance  # Corrected import

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'date']

class BalanceForm(forms.ModelForm):
    class Meta:
        model = UserBalance
        fields = ['balance']