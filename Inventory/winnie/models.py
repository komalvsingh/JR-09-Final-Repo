from django.db import models

class Signin(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    passw = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProductDetails(models.Model):
    proname = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.proname
