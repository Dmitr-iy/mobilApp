from rest_framework import serializers
from .models import Doctor, Location

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    def validate_latitude(self, value):
        if not -90 <= value <= 90:
            raise serializers.ValidationError("Неверное значение широты(должно быть от -90 до 90)")
        return value

    def validate_longitude(self, value):
        if not -180 <= value <= 180:
            raise serializers.ValidationError("Неверное значение долготы(должно быть от -180 до 180)")
        return value

    class Meta:
        model = Location
        fields = '__all__'

