from django.shortcuts import render, HttpResponse

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
