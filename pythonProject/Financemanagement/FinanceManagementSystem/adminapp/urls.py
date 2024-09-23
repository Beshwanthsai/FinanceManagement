from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.homepagecall,name='homepagecall'),
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/', views.logout, name='logout'),
    path('', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),

    path('expense_listpagecall/', views.expense_listpagecall, name='expense_listpagecall'),

    path('add_expensepagecall/', views.add_expensepagecall, name='add_expensepagecall'),

    path('delete_expensepagecall/', views.delete_expensepagecall, name='delete_expensepagecall'),
]

