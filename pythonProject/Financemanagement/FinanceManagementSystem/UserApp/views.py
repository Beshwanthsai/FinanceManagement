from django.shortcuts import render


# Create your views here.
def userhomepagecall(request):
    return render(request, 'UserApp/Userapphomepage.html')


# views.py
from django.shortcuts import render
from .models import Transaction

def balancecheckpagecall(request):
    transactions = Transaction.objects.filter(user=request.user)
    balance = sum(transaction.amount for transaction in transactions)
    return render(request, 'UserApp/checkBalance.html', {'balance': balance, 'transactions': transactions})

def addexpensepagecall(request):
    return render(request, 'UserApp/AddExpense.html')


# views.py
from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'UserApp/ExpenceList.html')
    else:
        form = ExpenseForm()
    return render(request, 'UserApp/AddExpense.html', {'form': form})


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'UserApp/ExpenceList.html', {'expenses': expenses})
