from rest_framework import serializers
from models import tra_pings, location, ping

class tra_pingsSerializer(serializers.Serializer):
    pin_id = serializers.CharField(required=False, read_only=True)
    numa = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    lat = serializers.FloatField(required=False)
    lon = serializers.FloatField(required=False)
    hora = serializers.CharField(required=False)

class locationSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, read_only=True)
    lat = serializers.FloatField(required=False)
    lon = serializers.FloatField(required=False)

class pingSerializer(serializers.Serializer):
    numa = serializers.CharField(required=False, read_only=True)
    name = serializers.CharField(required=False)
    lat = serializers.FloatField(required=False)
    lon = serializers.FloatField(required=False)
    hora = serializers.CharField(required=False)




# class ExampleDFRSerializer(serializers.Serializer):
#     example_id   = serializers.CharField(required=False, read_only=True)
#     example_type = serializers.IntegerField(required=False)
#     created_at   = serializers.DateTimeField(required=False)
#     description  = serializers.CharField(required=False)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return ExampleDFR.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.example_type = validated_data.get('example_type', instance.example_type)
#         instance.created_at = validated_data.get('created_at', instance.created_at)
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         return instance
