from django import template


register = template.Library()   #register is decorator here

@register.filter(name = 'is_in_cart')   #now, whenever 'is_in_cart' is used in template, this function will be called   
def is_in_cart(product,cart):
    keys = cart.keys()
    #print(keys)
    for id in keys:
        if int(id) == product.id:
            return True
        #print(product,cart)
    return False

@register.filter(name = 'get_count_of_Items')   #now, whenever 'get_count_of_Items' is used in template, this function will be called   
def get_count_of_Items(product,cart):
    keys = cart.keys()
    #print(keys)
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)    #returns value of product_id which is quantity. Cart = {product_id : Quantity}   <---- cart structure
        #print(product,cart)
    #return False

@register.filter(name = 'price_total')   #now, whenever 'price_total' is used in template, this function will be called   
def price_total(product,cart):
    total_price_of_item =  product.price * get_count_of_Items(product,cart)
    return total_price_of_item

@register.filter(name = "Total_CART_Price")
def Total_CART_Price(products,cart):
    total = 0
    for product in products:
        total = total + price_total(product,cart)
    return total

@register.filter(name = 'multipy')
def multiply(quantity,price):
    return quantity*price