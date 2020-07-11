from rest_framework import serializers
from .models import ProductSample

class ProductSampleSerializer(serializers.ModelSerializer):
    technology = serializers.StringRelatedField()
    service_type = serializers.StringRelatedField()

    class Meta :
        model = ProductSample
        fields = '__all__'
