import random
from django.core.management.base import BaseCommand
from sales.models import Product

class Command(BaseCommand):
    help = 'Seed the database with sample product data'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()  

        
        product_data = [
            {'name': 'Engine Oil', 'description': 'High-performance engine oil', 'price': 29.99},
            {'name': 'Brake Pads', 'description': 'Durable brake pads for all vehicles', 'price': 39.99},
            {'name': 'Air Filter', 'description': 'Premium air filter for improved engine performance', 'price': 14.99},
            
        ]

        for data in product_data:
            Product.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with product data'))
