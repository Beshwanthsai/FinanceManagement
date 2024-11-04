from django.urls import path
from . import views

app_name = 'UserApp'

urlpatterns = [
    path('userhomepagecall/', views.userhomepagecall, name='userhomepagecall'),
    path('check-balance/', views.balancecheckpagecall, name='balancecheckpagecall'),
    path('addexpensepagecall/', views.addexpensepagecall, name='addexpensepagecall'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('expense_list/', views.expense_list, name='expense_list'),
    path('set_balance/', views.set_balance, name='set_balance'),
    path('expenses_by_month_form/', views.expenses_by_month_form, name='expenses_by_month_form'),
    path('expenses_by_month/', views.expenses_by_month, name='expenses_by_month'),
]