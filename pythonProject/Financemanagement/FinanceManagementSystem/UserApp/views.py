from django.shortcuts import render

# Create your views here.
def userhomepagecall(request):
    return render(request, 'UserApp/Userapphomepage.html')

def balancecheckpagecall(request):
    return render(request,'UserApp/checkBalance.html')

def addexpensepagecall(request):
    return render(request,'UserApp/AddExpense.html')

# views.py
from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('UserApp:ExpenceList')
    else:
        form = ExpenseForm()
    return render(request, 'UserApp/AddExpense.html', {'form': form})

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'UserApp/ExpenceList.html', {'expenses': expenses})