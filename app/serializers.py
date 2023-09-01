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


# from rest_framework import serializers
# from .models import Location, Doctor
#
# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = ['doctor', 'latitude', 'longitude', 'timestamp']
#
# # class DoctorSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Doctor
# #         fields = ['doctor_id', 'name']
#
# class LocationCreateSerializer(serializers.ModelSerializer):
#     location = LocationSerializer()
#
#     class Meta:
#         model = Doctor
#         fields = '__all__'
#         read_only_fields = ['doctor_id']
#
#         def create(self, validated_data):
#             location_data = validated_data.pop('location')
#
#             location = Location.objects.get(**location_data)
#             instance = Doctor.objects.create(location=location, **validated_data)
#             instance.save()
#
#             return instance

# def create(self, validated_data):
#     location_data = validated_data.pop('location')
#     doctor = Doctor.objects.create(**validated_data)
#     try:
#         Location.objects.create(doctor=doctor, **location_data)
#     except Exception as e:
#         doctor.delete()
#         raise e
#     return doctor