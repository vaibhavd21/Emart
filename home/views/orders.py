
from home.models.customer import Customer
from django.shortcuts import redirect, render , HttpResponse
from home.models.customer import Customer
from home.models.product import Product
from home.models.category import Category
from django.contrib.auth.hashers import  check_password
from django.views import  View
from home.models.product import Product
from home.models.orders import Orders


class Order(View):
    def get(self,request):
        customer = request.session.get('customer_id')
        orders = Orders.get_orders_by_cust_id(customer)
        #print(orders)
        return render(request,'orders.html',{'orders':orders})