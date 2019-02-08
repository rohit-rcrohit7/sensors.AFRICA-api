from rest_framework import serializers


class ReadingsSerializer(serializers.Serializer):
    average = serializers.FloatField()
    minimum = serializers.FloatField()
    maximum = serializers.FloatField()
    day = serializers.DateTimeField()
    value_type = serializers.CharField(max_length=200)