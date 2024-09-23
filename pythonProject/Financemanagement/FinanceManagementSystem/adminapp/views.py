from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def homepagecall(request):
    return render(request,'adminapp/projecthomepage.html')

def UserLoginPageCall(request):
    return render(request, 'adminapp/Login.html')
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        auth.login(request,user)
        if user is not None:
            # Check the length of the username
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as Beshwanth Sai Katari!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
            elif len(username) ==4 :
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as user!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/Login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/Login.html')
    else:
        return render(request, 'adminapp/Login.html')

def UserRegisterPageCall(request):
    return render(request, 'adminapp/Register.html')


def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/Register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/Register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/Register.html')
    else:
        return render(request, 'adminapp/Register.html')


def logout(request):
    auth.logout(request)
    return redirect('homepagecall')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm



def expense_listpagecall(request):
    return render(request, 'adminapp/expense_list.html')
# View to display all expenses



def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    total_expense = sum(exp.amount for exp in expenses)
    return render(request, 'adminapp/expense_list.html', {'expenses': expenses, 'total_expense': total_expense})





def add_expensepagecall(request):
    return render(request, 'adminapp/add_expense.html')
# View to handle new expense creation




def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')  # After saving, redirect to the list view
    else:
        form = ExpenseForm()

    return render(request, 'adminapp/add_expense.html', {'form': form})




def delete_expensepagecall(request):
    return render(request, 'adminapp/delete_expense.html')
# View to delete an expense



def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')

    return render(request, 'adminapp/delete_expense.html', {'expense': expense})
