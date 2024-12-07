from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense, UserBalance  # Corrected import
from .forms import ExpenseForm, BalanceForm
from django.db.models import Sum

def userhomepagecall(request):
    return render(request, 'UserApp/Userapphomepage.html')

def addexpensepagecall(request):
    return render(request, 'UserApp/AddExpense.html')

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('UserApp:expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'UserApp/AddExpense.html', {'form': form})


from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import UserBalance


def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    total_expenses = sum(expense.amount for expense in expenses)

    try:
        user_balance = UserBalance.objects.get(user=request.user)
    except UserBalance.DoesNotExist:
        user_balance = None  # or handle it in another way, e.g., create a new UserBalance object

    remaining_balance = user_balance.balance - total_expenses if user_balance else 0

    return render(request, 'UserApp/ExpenceList.html', {
        'expenses': expenses,
        'total_expenses': total_expenses,
        'remaining_balance': remaining_balance
    })
def balancecheckpagecall(request):
    user_balance = UserBalance.objects.get(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    total_expenses = sum(expense.amount for expense in expenses)
    remaining_balance = user_balance.balance - total_expenses
    return render(request, 'UserApp/checkBalance.html', {'balance': user_balance, 'remaining_balance': remaining_balance})

@login_required
def set_balance(request):
    user = request.user
    if request.method == 'POST':
        balance = float(request.POST['balance'])
        user_balance, created = UserBalance.objects.get_or_create(user=user)
        user_balance.balance += balance
        user_balance.save()
        return redirect('UserApp:set_balance')

    user_balance, created = UserBalance.objects.get_or_create(user=user)
    expenses = Expense.objects.filter(user=user)
    total_expenses = sum(expense.amount for expense in expenses)
    remaining_balance = user_balance.balance - total_expenses

    context = {
        'current_balance': user_balance.balance,
        'remaining_balance': remaining_balance
    }
    return render(request, 'UserApp/SetBalance.html', context)

def expenses_by_month_form(request):
    return render(request, 'UserApp/ExpensesByMonthForm.html')

def expenses_by_month(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    if year and month:
        expenses = Expense.objects.filter(user=request.user, date__year=year, date__month=month)
        total_amount = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    else:
        expenses = []
        total_amount = 0
    return render(request, 'UserApp/ExpensesByMonth.html', {'expenses': expenses, 'total_amount': total_amount, 'year': year, 'month': month})