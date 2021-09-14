from rest_framework import viewsets
from . import models
from . import serializers

class CustomerViewset(viewsets.ModelViewSet):
    queryset = models.Customers.objects.all()
    serializer_class = serializers.Customerserializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = models.Products.objects.all()
    serializer_class = serializers.Productserializer

class Order_itemViewset(viewsets.ModelViewSet):
    queryset = models.Order_items.objects.all()
    serializer_class = serializers.Order_itemserializer

class OrderViewset(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.Orderserializer