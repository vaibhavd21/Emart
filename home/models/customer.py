from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=12,default='...')
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    email = models.EmailField()
    pass1 = models.CharField(max_length=254)
    pass2 = models.CharField(max_length=254,default='')
    
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_username(username):
        return Customer.objects.get(username = username)

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return  False
