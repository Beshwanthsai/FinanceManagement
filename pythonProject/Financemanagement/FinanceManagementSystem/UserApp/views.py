from django.shortcuts import render


# Create your views here.
def userhomepagecall(request):
    return render(request, 'UserApp/Userapphomepage.html')

def addexpensepagecall(request):
    return render(request, 'UserApp/AddExpense.html')
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Expense, Balance
from .forms import ExpenseForm, BalanceForm

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.balance = Balance.objects.first()
            expense.save()
            return redirect(reverse('UserApp:expense_list'))
    else:
        form = ExpenseForm()
    return render(request, 'UserApp/AddExpense.html', {'form': form})

def expense_list(request):
    expenses = Expense.objects.all()
    total_expenses = sum(expense.amount for expense in expenses)
    balance = Balance.objects.first()
    remaining_balance = balance.initial_balance - total_expenses if balance else 0
    return render(request, 'UserApp/ExpenceList.html', {'expenses': expenses, 'total_expenses': total_expenses, 'remaining_balance': remaining_balance})

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

from django.shortcuts import render
from django.db.models import Sum
from .models import Expense
from datetime import datetime

from django.shortcuts import render
from django.db.models import Sum
from .models import Expense

def expenses_by_month_form(request):
    return render(request, 'UserApp/ExpensesByMonthForm.html')

def expenses_by_month(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    if year and month:
        expenses = Expense.objects.filter(date__year=year, date__month=month)
        total_amount = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    else:
        expenses = []
        total_amount = 0
    return render(request, 'UserApp/ExpensesByMonth.html', {'expenses': expenses, 'total_amount': total_amount, 'year': year, 'month': month})