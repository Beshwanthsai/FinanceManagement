from django.urls import path,include
from . import views
app_name = 'UserApp'

urlpatterns = [
    path('userhomepage/', views.userhomepagecall, name='userhomepage'),
]
