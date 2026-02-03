from rest_framework import serializers
from products.models import Producto

class TeachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            
        ]