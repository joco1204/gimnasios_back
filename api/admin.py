from django.contrib import admin
from .models import TipoIdentificacion, StatusReservation, User, PhotoRegister, Reservation, AccessGym

# Register your models here.
admin.site.register(TipoIdentificacion)
admin.site.register(StatusReservation)
admin.site.register(User)
admin.site.register(PhotoRegister)
admin.site.register(Reservation)
admin.site.register(AccessGym)
