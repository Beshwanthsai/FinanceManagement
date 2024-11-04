from django.shortcuts import render


# Create your views here.
def userhomepagecall(request):
    return render(request, 'UserApp/Userapphomepage.html')

def addexpensepagecall(request):
    return render(request, 'UserApp/AddExpense.html')

# here

# views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Expense, Balance
from .forms import ExpenseForm, BalanceForm

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('UserApp:expense_list'))
    else:
        form = ExpenseForm()
    return render(request, 'UserApp/AddExpense.html', {'form': form})

def expense_list(request):
    expenses = Expense.objects.all()
    total_expenses = sum(expense.amount for expense in expenses)
    return render(request, 'UserApp/ExpenceList.html', {'expenses': expenses, 'total_expenses': total_expenses})

def balancecheckpagecall(request):
    balance = Balance.objects.first()
    expenses = Expense.objects.all()
    total_expenses = sum(expense.amount for expense in expenses)
    remaining_balance = balance.initial_balance - total_expenses if balance else 0
    return render(request, 'UserApp/checkBalance.html', {'balance': balance, 'remaining_balance': remaining_balance})

def set_balance(request):
    if request.method == 'POST':
        form = BalanceForm(request.POST)
        if form.is_valid():
            Balance.objects.all().delete()  # Ensure only one balance record exists
            form.save()
            return redirect(reverse('UserApp:balancecheckpagecall'))
    else:
        form = BalanceForm()
    return render(request, 'UserApp/SetBalance.html', {'form': form})