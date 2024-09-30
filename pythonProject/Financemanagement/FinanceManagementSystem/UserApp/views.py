from django.shortcuts import render

# Create your views here.
def userhomepagecall(request):
    return render(request, 'UserApp/Userapphomepage.html')

def balancecheckpagecall(request):
    return render(request,'UserApp/checkBalance.html')

def addexpensepagecall(request):
    return render(request,'UserApp/AddExpense.html')