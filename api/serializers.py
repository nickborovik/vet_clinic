from rest_framework import serializers
from core.models import Animal, AnimalType, Appointment


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'


class AnimalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalType
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
