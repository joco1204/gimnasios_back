from rest_framework import viewsets
from .serializer import TipoIdentificacionSerializer, StatusReservationSerializer, UserSerializer, PhotoRegisterSerializer, ReservationSerializer, AccessGymSerializer
from .models import TipoIdentificacion, StatusReservation, User, PhotoRegister, Reservation, AccessGym

# Create your views here.
class TipoIdentificacionViewSet(viewsets.ModelViewSet):
    queryset = TipoIdentificacion.objects.all()
    serializer_class = TipoIdentificacionSerializer

class StatusReservationViewSet(viewsets.ModelViewSet):
    queryset = StatusReservation.objects.all()
    serializer_class = StatusReservationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PhotoRegisterViewSet(viewsets.ModelViewSet):
    queryset = PhotoRegister.objects.all()
    serializer_class = PhotoRegisterSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class AccessGymViewSet(viewsets.ModelViewSet):
    queryset = AccessGym.objects.all()
    serializer_class = AccessGymSerializer