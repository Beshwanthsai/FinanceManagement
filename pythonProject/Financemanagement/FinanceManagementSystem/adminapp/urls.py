from tkinter.font import names

from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.homepagecall,name='homepagecall'),
    path('Loginpagecall/',views.Loginpagecall,name='Loginpagecall'),
    path('Registerpagecall/',views.Registerpagecall,name='Registerpagecall'),
]

