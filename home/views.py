from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Welcome to Homepage!")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("About page")

def services(request):
    #return HttpResponse("Services page")
    return render(request, 'services.html')

def contact(request):
    #return HttpResponse("Contact page")
    return render(request, 'contact.html')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)>10:
            messages.info(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')

        if (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname

        myuser.save()
        
        messages.success(request, "Account successfully created!")
        return redirect('home')
        
    else:
        return HttpResponse("404 - Not found")

def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Logged In Successful")
            return redirect('home')

        else:
            messages.error(request,"Invalid Input")
            return HttpResponse("404 :(")
            
        
    return HttpResponse("Not found :-(")

def handleLogout(request):
    logout(request)
    messages.success(request,"Logged Out Successful")
    return redirect('home')



    #return HttpResponse("handleLogout")