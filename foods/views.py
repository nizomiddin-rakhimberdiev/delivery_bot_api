from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product,UserLocation,Category,Client, Cart, Order, OrderItem
from .serializers import CartSerializer, ProductSerializer, UserLocationSerializer, CategorySerializer,ClientSerializer, OrderSerializer, OrderItemSerializer




class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailAPIView(APIView):
    def get(self, request, pk): 
        product = Product.objects.get(pk=pk)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserLocationListAPIView(APIView):
    def get(self, request):
        locations = UserLocation.objects.all()
        serializer = UserLocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLocationDetailAPIView(APIView):
    def get(self, request, pk): 
        location = self.get_object(pk)
        if location is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserLocationSerializer(location)
        return Response(serializer.data)
    def put(self, request, pk):
        location = self.get_object(pk)
        if location is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserLocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        location = self.get_object(pk)
        if location is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryDetailAPIView(APIView):
    def get(self, request, pk): 
        category = self.get_object(pk)
        if category is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, pk):
        category = self.get_object(pk)
        if category is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        category = self.get_object(pk)
        if category is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ClientListAPIView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClientDetailAPIView(APIView):
    def get(self, request, pk): 
        client = Client.objects.get(pk=pk)
        if client is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    def put(self, request, pk):
        client = Client.objects.get(pk=pk)
        if client is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        client = Client.objects.get(pk=pk)
        if client is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CartListAPIView(APIView):
    def get(self, request, user_id):
        carts = Cart.objects.filter(user__user_id=user_id)
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)


class AddCartAPIView(APIView):
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartDetailAPIView(APIView):
    def get(self, request, pk): 
        cart = Cart.objects.get(pk=pk)
        if cart is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    def put(self, request, pk):
        cart = Cart.objects.get(pk=pk)
        if cart is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        cart = Cart.objects.get(pk=pk)
        if cart is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class OrderListCreateAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # products_data = request.data.get('products', [])
            # for item in products_data:
            #     product_id = item.get('product')
            #     quantity = item.get('quantity', 1)
            #     product = Product.objects.get(id=product_id)
            #     OrderItem.objects.create(order=order, product=product, quantity=quantity)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderDetailAPIView(APIView):
    def get(self, request, pk): 
        order = Order.objects.get(pk=pk)
        if order is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    def put(self, request, pk):
        order = Order.objects.get(pk=pk)
        if order is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        order = Order.objects.get(pk=pk)
        if order is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class OrderItemListAPIView(APIView):
    def get(self, request):
        order_items = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderItemDetailAPIView(APIView):
    def get(self, request, pk): 
        order_item = OrderItem.objects.get(pk=pk)
        if order_item is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)
    def put(self, request, pk):
        order_item = OrderItem.objects.get(pk=pk)
        if order_item is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderItemSerializer(order_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        order_item = OrderItem.objects.get(pk=pk)
        if order_item is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        order_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ClearCartAPIView(APIView):
    def delete(self, request, user_id):
        carts = Cart.objects.filter(user__user_id=user_id)
        carts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

