from rest_framework import serializers
from .models import Client, UserLocation, Category, Product, Cart, Order, OrderItem


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    # user = ClientSerializer(read_only=True)
    # items = OrderItemSerializer(source='orderitem_set', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'total_price', 'address', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']
    # def create(self, validated_data):
    #     items_data = self.initial_data.get('products')
    #     order = Order.objects.create(**validated_data)
    #     for item in items_data:
    #         product = Product.objects.get(id=item['product'])
    #         OrderItem.objects.create(order=order, product=product, quantity=item['quantity'])
    #     return order