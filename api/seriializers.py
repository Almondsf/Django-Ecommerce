from rest_framework import serializers
from .models import Order, OrderItem, Product


class ProductSerializzer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'stock'
        )
        
        def validate_price(self, value):
            if value <= 0:
                raise serializers.ValidationError(
                    "Price must be greater than zero"
                )
            return value
            