
from django.contrib.auth import logout
from django.shortcuts import redirect

def handleLogout(request):
    request.session.clear()
    #messages.success(request,"Logged Out Successful")
    return redirect('home')

