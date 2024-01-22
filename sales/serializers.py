from rest_framework import serializers
from .models import Product, ShoppingCart, Order, Client

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

class ShoppingCartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = ShoppingCart
        fields = ['id', 'client', 'products']

class OrderSerializer(serializers.ModelSerializer):
    shopping_cart = ShoppingCartSerializer()

    class Meta:
        model = Order
        fields = ['id', 'shopping_cart', 'delivery_date']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email']

