#from home.models.customer import Customer
from home.models.category import Category
from home.models.product import Product
#from django.views import View
from django.shortcuts import redirect, render


def index(request):
    if request.method == "POST":
        product = request.POST.get('product')
        remove = request.POST.get('remove_item')
        cart = request.session.get('cart')
        if cart: 
            qnty = cart.get(product)   #getting of value(i.e. qnty) of the product(product is the key in CART dict whose value is quantity) 
            if qnty:
                if remove:   #we will get remove if we click on '-' sign 
                    if qnty<=1:
                        cart.pop(product)
                    else:
                        cart[product] = qnty - 1
                else:
                    cart[product] = qnty + 1 #if click on '+' increase the qnty by 1 
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1
        
        request.session['cart'] = cart

        #print(request.session['cart']) 
        #print(product)
        return redirect('home')

    if request.method == "GET":

        cart = request.session.get('cart')   #get the cart for the current session
        if not cart:                         #if there is no cart for a current session, make a empty cart
            request.session['cart'] = {}

        #print(request.session.get('cart'))
        products = None
        #request.session.get('cart').clear()
        Categories = Category.get_all_categories()
        #print(products)

        CategoryId = request.GET.get('category')   #getting this from url
        if CategoryId:
            products = Product.get_all_products_byCatID(CategoryId)
            
        else:
            products = Product.get_all_products()

        
        print(request.session.get('customer_username'))

        if request.session.get('customer_username') == None:
            data = {'products' : products,'categories':Categories}
            return render(request, 'index.html',data)
        else:
            data = {'products' : products,'categories':Categories,'name':request.session.get('customer_username')}
            return render(request, 'index.html', data)
        #return HttpResponse("Welcome to Homepage!")