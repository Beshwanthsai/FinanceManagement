from django import forms
from .models import Expense, Balance

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'date']

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['initial_balance']