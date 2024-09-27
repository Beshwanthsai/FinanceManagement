from django.shortcuts import render

# Create your views here.
def userhomepagecall(request):
    return render(request, 'UserApp/Userapphomepage.html')