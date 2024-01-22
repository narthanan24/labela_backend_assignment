from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'sales'

class ShoppingCart(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

class Order(models.Model):
    shopping_cart = models.OneToOneField(ShoppingCart, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField()

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
