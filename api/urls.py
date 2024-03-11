from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'tipo-tidentificacion', views.TipoIdentificacionViewSet, basename='tipo-identificacion')
router.register(r'status-reservatio', views.StatusReservationViewSet, basename='status-reservatio')
router.register(r'photo-register', views.PhotoRegisterViewSet, basename='photo-register')
router.register(r'reservation', views.ReservationViewSet, basename='reservation')
router.register(r'access-gym', views.AccessGymViewSet, basename='access-gym')

urlpatterns = [
    path('', include(router.urls))
]