from dataclasses import fields
from rest_framework import serializers
from .models import Products, Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"