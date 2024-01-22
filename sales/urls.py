from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ShoppingCartViewSet, OrderViewSet, ClientViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'shopping-carts', ShoppingCartViewSet, basename='shopping-cart')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'clients', ClientViewSet, basename='client')

urlpatterns = [
    path('api/', include(router.urls)),
]

urlpatterns += [
    path('api/clients/<int:pk>/add-to-cart/', ClientViewSet.as_view({'post': 'add_to_cart'}), name='client-add-to-cart'),
    path('api/clients/<int:pk>/remove-from-cart/', ClientViewSet.as_view({'post': 'remove_from_cart'}), name='client-remove-from-cart'),
    path('api/clients/<int:pk>/place-order/', ClientViewSet.as_view({'post': 'place_order'}), name='client-place-order'),
]
