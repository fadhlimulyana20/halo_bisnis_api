from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()
    category = serializers.StringRelatedField(many=True)
    # updated_at = serializers.DateTimeField(format="%f")

    class Meta:
        model = Product
        fields = [
            'id', 
            'name', 
            'price', 
            'description', 
            'created_at', 
            'cover', 
            'type', 
            'category', 
            'version', 
            'active', 
            'featured',
            'updated_at',
            'framework'
        ]