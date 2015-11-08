from rest_framework import serializers
from .models import Room, Booking, Guest


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
