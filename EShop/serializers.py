from rest_framework import serializers
from .models import Customers, Products, Order_items, Order


class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class Order_itemserializer(serializers.ModelSerializer):
    class Meta:
        model = Order_items
        fields = '__all__'

class Orderserializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

