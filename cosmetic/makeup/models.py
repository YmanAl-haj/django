from django.db import models

# Create your models here.


class Brand(models.Model):
    """
        this tag in brand model test
        """
    name = models.CharField(max_length=30)
    origin = models.TextField()

    def __str__(self):
        return "Name is: {} \n Origin is: {}".format(self.name, self.orgin)

    def get_absolute_url(self):
        pass


class Products(models.Model):
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=30)
    description = models.TextField()
    pub_date = models.DateField('expire date')
    price=models.IntegerField()
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)


    def __str__(self):
        return "Name is: {}\n Kind is: {}\n Price is: {}\n Brand is: {}".format(self.name, self.kind,self.price,self.brand)

    def get_absolute_url(self):
        pass

