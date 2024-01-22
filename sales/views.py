from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product, ShoppingCart, Order, Client
from .serializers import ProductSerializer, ShoppingCartSerializer, OrderSerializer, ClientSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        client = self.get_object()
        product_id = request.data.get('product_id')
        product = Product.objects.get(pk=product_id)

        shopping_cart, created = ShoppingCart.objects.get_or_create(client=client)
        shopping_cart.products.add(product)

        return Response({'status': 'Product added to the shopping cart successfully'})

    @action(detail=True, methods=['post'])
    def remove_from_cart(self, request, pk=None):
        client = self.get_object()
        product_id = request.data.get('product_id')
        product = Product.objects.get(pk=product_id)

        shopping_cart = ShoppingCart.objects.get(client=client)
        shopping_cart.products.remove(product)

        return Response({'status': 'Product removed from the shopping cart successfully'})

    @action(detail=True, methods=['post'])
    def place_order(self, request, pk=None):
        client = self.get_object()

        shopping_cart = ShoppingCart.objects.get(client=client)
        delivery_date = request.data.get('delivery_date')

        order = Order.objects.create(shopping_cart=shopping_cart, delivery_date=delivery_date)

        return Response({'status': 'Order placed successfully'})
