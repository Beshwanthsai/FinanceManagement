# urls.py
from django.urls import path
from . import views

app_name = 'UserApp'

urlpatterns = [
    path('userhomepagecall/', views.userhomepagecall, name='userhomepagecall'),
    path('check-balance/', views.balancecheckpagecall, name='balancecheckpagecall'),
    path('addexpensepagecall/', views.addexpensepagecall, name='addexpensepagecall'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('expense_list/', views.expense_list, name='expense_list'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),  # Add this line
]