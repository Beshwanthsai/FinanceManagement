from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepagecall, name='homepagecall'),
    path('Loginpagecall/', views.Loginpagecall, name='Loginpagecall'),
    path('Registerpagecall/', views.Registerpagecall, name='Registerpagecall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('logout/', views.logout_view, name='logout'),
    path('all_users_expenses/', views.all_users_expenses, name='all_users_expenses'),
]