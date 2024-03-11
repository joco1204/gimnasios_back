from rest_framework import serializers
from .models import TipoIdentificacion, StatusReservation, User, PhotoRegister, Reservation, AccessGym  

class TipoIdentificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIdentificacion
        fields = '__all__'

class StatusReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusReservation
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PhotoRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoRegister
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class AccessGymSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessGym
        fields = '__all__'
