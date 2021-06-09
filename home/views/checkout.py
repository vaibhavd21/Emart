
from home.models.customer import Customer
from django.shortcuts import redirect, render , HttpResponse
from home.models.customer import Customer
from home.models.product import Product
from home.models.category import Category
from django.contrib.auth.hashers import  check_password
from django.views import  View
from home.models.product import Product
from home.models.orders import Orders


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        ids = list(cart.keys())
        product_objects = Product.get_product_by_ProductID(ids)
        #print(address,phone,customer,cart,product_objects)

        for product in product_objects:
            order = Orders(customer = Customer(id = customer), 
                            product = product, 
                            price = product.price,
                            address = address,
                            phone = phone, 
                            quantity = cart.get(str(product.id)),
                            status = True
                            )
            order.place_order()
        request.session['cart'] = {}

        return redirect('cart')