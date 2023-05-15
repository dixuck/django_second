from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 23)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=23, decimal_places=2)
    checkk = serializers.BooleanField()
