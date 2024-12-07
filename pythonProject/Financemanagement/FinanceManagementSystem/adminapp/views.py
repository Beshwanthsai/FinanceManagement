
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def homepagecall(request):
    return render(request, 'adminapp/projecthomepage.html')

def Loginpagecall(request):
    return render(request, 'adminapp/Login.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Check the length of the username
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as User!')
                return redirect('UserApp:userhomepagecall')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as Finance Manager!')
                return redirect('UserApp:userhomepagecall')
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

def Registerpagecall(request):
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
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/Register.html')
    else:
        return render(request, 'adminapp/Register.html')

def logout_view(request):
    logout(request)
    return redirect('homepagecall')

from django.shortcuts import render
from UserApp.models import User, Expense, UserBalance

def all_users_expenses(request):
    users_data = []
    users = User.objects.all()
    for user in users:
        expenses = Expense.objects.filter(user=user)
        total_expenses = sum(expense.amount for expense in expenses)
        try:
            user_balance = UserBalance.objects.get(user=user)
        except UserBalance.DoesNotExist:
            user_balance = None
        remaining_balance = user_balance.balance - total_expenses if user_balance else 0
        users_data.append({
            'user': user,
            'expenses': expenses,
            'total_expenses': total_expenses,
            'remaining_balance': remaining_balance
        })
    return render(request, 'adminapp/all_users_expenses.html', {'users_data': users_data})

# views.py
from django.shortcuts import render
from django.contrib.auth.models import User
from UserApp.models import Expense

def search_users(request):
    query = request.GET.get('query')
    users = User.objects.none()  # Default to an empty queryset
    no_results = False
    user_expenses = None
    total_expenses = 0

    if query:
        users = User.objects.filter(username__icontains=query) | User.objects.filter(email__icontains=query) | User.objects.filter(first_name__icontains=query) | User.objects.filter(last_name__icontains=query)
        if not users.exists():
            no_results = True
        elif users.count() == 1:
            user = users.first()
            user_expenses = Expense.objects.filter(user=user)
            total_expenses = sum(expense.amount for expense in user_expenses)

    return render(request, 'adminapp/search_users.html', {
        'users': users,
        'no_results': no_results,
        'user_expenses': user_expenses,
        'total_expenses': total_expenses
    })