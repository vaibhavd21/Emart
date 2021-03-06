from django.conf.urls.static import static
from home.models.category import Category
from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=150,default='')
    image = models.ImageField(upload_to = 'uploads/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_byCatID(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_product_by_ProductID(product_ids):   #product_ids is the list coming from cart.py
        return Product.objects.filter(id__in = product_ids)  #returns all the products in product_ids