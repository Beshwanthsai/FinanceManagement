from django.urls import path,include
from . import views
app_name = 'UserApp'

urlpatterns = [
    path('userhomepagecall/', views.userhomepagecall, name='userhomepagecall'),
    path('balancecheckpagecall/', views.balancecheckpagecall, name='balancecheckpagecall'),
    path('addexpensepagecall/', views.addexpensepagecall, name='addexpensepagecall'),
]
