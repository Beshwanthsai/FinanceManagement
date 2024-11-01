from django.shortcuts import render


# Create your views here.
def userhomepagecall(request):
    return render(request, 'UserApp/Userapphomepage.html')


def balancecheckpagecall(request):
    return render(request, 'UserApp/checkBalance.html')
def addexpensepagecall(request):
    return render(request, 'UserApp/AddExpense.html')


# views.py
from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

# views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Expense
from .forms import ExpenseForm

# views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Expense
from .forms import ExpenseForm

# views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Expense
from .forms import ExpenseForm

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


# views.py
from django.shortcuts import render

def add_transaction(request):
    # Your logic for adding a transaction
    return render(request, 'UserApp/AddTransaction.html')