
from home.models.customer import Customer
from django.shortcuts import redirect, render , HttpResponse
from home.models.customer import Customer
from home.models.product import Product
from home.models.category import Category
from django.contrib.auth.hashers import  check_password
from django.views import  View
from home.models.product import Product

class cart(View):
    def get(self,request):
        #print(request.session.get('cart'))  this is cart for the current session (cart is dict with key as product_id and its value is quantity of items in cart)
        product_ids_in_cart =  list(request.session.get('cart').keys()) 
        product_objects_in_cart = Product.get_product_by_ProductID(product_ids_in_cart)
        print(product_objects_in_cart)
        return render(request,'cart.html',{'products':product_objects_in_cart})