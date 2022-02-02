from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Brand(models.Model):
    """
        this tag in brand model test
        """
    name = models.CharField(max_length=30)
    origin = models.CharField(max_length=30)

    def __str__(self):
        return "Name: {} \n Origin: {}".format(self.name, self.origin)

    def get_absolute_url(self):
        pass


class Products(models.Model):
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=30)
    description = models.TextField()
    pub_date = models.DateField('expire date')
    price=models.IntegerField()
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images")


    def __str__(self):
        return "Name: {}\n Kind: {}\n Price: {}\n Brand: {}".format(self.name, self.kind,self.price,self.brand)

    def get_absolute_url(self):
        pass
class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)


# class Shipping(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200)
#     payment=models.CharField(max_length=50,null=True)
#     order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
#
#     def __str__(self):
#         return self.name