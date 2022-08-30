from rest_framework import serializers
from .models import CarPrice


class CarPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPrice
        fields = '__all__'