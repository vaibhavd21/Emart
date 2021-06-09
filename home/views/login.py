
from home.models.customer import Customer
from django.shortcuts import redirect, render , HttpResponse
from home.models.customer import Customer
from home.models.product import Product
from home.models.category import Category
from django.contrib.auth.hashers import  check_password
from django.views import  View


class login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        data = login.getdata(request)

        cust = Customer.get_customer_by_username(loginusername)
        error_msg = None
        if cust:
            flag = check_password(loginpassword, cust.pass1)
            usern = cust.username
            #data['name'] = usern
            #data['data'] = flag
            if flag:
                request.session['customer_id'] = cust.id
                request.session['customer_username'] = cust.username
                return redirect('home')
            else:
                return HttpResponse("Something Invalid")

        else:
            return HttpResponse("Something Invalid")
 
    @staticmethod
    def getdata(request):
        products = None
        Categories = Category.get_all_categories()
        #print(products)

        CategoryId = request.GET.get('category')   #getting this from url
        if CategoryId:
            products = Product.get_all_products_byCatID(CategoryId)
            
        else:
            products = Product.get_all_products()

        return {'products' : products,'categories':Categories}