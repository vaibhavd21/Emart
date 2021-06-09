from django.http.response import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from home.models.customer import Customer

class handleSignUp(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self,request):
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        error_message = None

        customer = Customer(username=username, 
                            fname=fname,
                            lname=lname,
                            email=email,
                            pass1=pass1,
                            pass2=pass2)
        error_message = self.validateCustomer(customer)

        
        # Create the user
        if not error_message:
            customer.pass1 = make_password(customer.pass1)
            customer.pass2 = make_password(customer.pass2)
            customer.register()
            return redirect('home')
        #myuser.save()
        #return redirect('home')
        else:
            return HttpResponse(error_message)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.fname):
            error_message = "First Name Required !!"
        elif not customer.lname:
            error_message = 'Last Name Required'
        elif not customer.email:
            error_message = 'Email id required'
        elif len(customer.pass1) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        elif customer.pass1 != customer.pass2:
            error_message = 'Password Not Matching'

        return error_message