from django.urls import path
from .views import (
    ProductListAPIView, ProductDetailAPIView,
    UserLocationListAPIView, UserLocationDetailAPIView,
    CategoryListAPIView, CategoryDetailAPIView,
    ClientListAPIView, ClientDetailAPIView
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
]