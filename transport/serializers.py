from rest_framework import serializers
from .models import TransportOrganizer, Vehicle, Booking, TransportOption
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user


class TransportOrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportOrganizer
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['student', 'created_at', 'is_paid']

class TransportOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportOption
        fields = '__all__'
        read_only_fields = ['organizer', 'approved']