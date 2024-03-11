from django.db import models

# Create your models here.

class TipoIdentificacion(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class StatusReservation(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status

class User(models.Model):
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE)
    numero_identificacion = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=150, null=True, blank=True)
    active = models.BooleanField(default=True)

class PhotoRegister(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.TextField()
    active = models.BooleanField(default=True)

class Reservation(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_photo = models.ForeignKey(PhotoRegister, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date= models.DateTimeField()
    status = models.ForeignKey(StatusReservation, on_delete=models.CASCADE)

class AccessGym(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    access_date = models.DateTimeField()
    exit_date= models.DateTimeField()