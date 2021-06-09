from django.contrib import admin
from django.urls import path,include
from .views.handleSignUp import handleSignUp
from .views.login import login
from .views.logout import handleLogout
from .views.contact import contact
from .views.index import index
from .views.cart import cart
from .views.checkout import CheckOut
from .views.orders import Order

urlpatterns = [
    path("",index, name='home'),
    path("contact",contact, name='contact'),
    path("signup",handleSignUp.as_view(), name='handleSignUp'),
    path("login",login.as_view(), name='handleLogin'),
    path("logout",handleLogout, name='handleLogout'),
    path("cart",cart.as_view(), name='cart'),
    path('checkout',CheckOut.as_view(),name='checkout'),
    path('orders',Order.as_view(),name='orders')
]
