from django.shortcuts import render
def contact(request):
    #return HttpResponse("Contact page")
    return render(request, 'contact.html')