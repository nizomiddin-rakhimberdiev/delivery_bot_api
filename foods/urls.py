from django.urls import path
from .views import (
    ProductListAPIView, ProductDetailAPIView,
    UserLocationListAPIView, UserLocationDetailAPIView,
    CategoryListAPIView, CategoryDetailAPIView,
    ClientListAPIView, ClientDetailAPIView, CartListAPIView, CartDetailAPIView,
    AddCartAPIView, ClearCartAPIView, OrderListCreateAPIView, OrderDetailAPIView, OrderItemListAPIView, OrderItemDetailAPIView
)

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('locations/', UserLocationListAPIView.as_view(), name='location-list'),
    path('locations/<int:pk>/', UserLocationDetailAPIView.as_view(), name='location-detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('clients/', ClientListAPIView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailAPIView.as_view(), name='client-detail'),
    path('cart/<str:user_id>/', CartListAPIView.as_view(), name='cart-list'),
    path('cart/', AddCartAPIView.as_view(), name='add-cart'),
    path('carts/<int:pk>/', CartDetailAPIView.as_view(), name='cart-detail'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('order-items/', OrderItemListAPIView.as_view(), name='orderitem-list'),
    path('order-items/<int:pk>/', OrderItemDetailAPIView.as_view(), name='orderitem-detail'),
    path('cart/clear/<str:user_id>/', ClearCartAPIView.as_view(), name='clear-cart'),
]