
from django.db import models
from django.db.models.deletion import CASCADE
from .product import Product
from .customer import Customer
import datetime

class Orders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=250,default='',blank=True)
    phone = models.CharField(max_length=12,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)



    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_cust_id(customer_id):
        return Orders.objects.filter(customer = customer_id).order_by('-date') #order by descending order of date