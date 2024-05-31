from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClinicViewSet, BedViewSet, ClinicRoomViewSet, create_bed, create_clinic_room, list_beds_by_room_number, list_clinic_rooms_by_clinic_name, update_clinic_room_by_clinic_name, delete_clinic_room_by_clinic_name

router = DefaultRouter()
router.register(r'clinics', ClinicViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('clinic-rooms/create', create_clinic_room, name='create_clinic_room'),
    path('clinic-rooms/read', list_clinic_rooms_by_clinic_name, name='clinic_rooms_by_clinic_name'),
    path('clinic-rooms/update/', update_clinic_room_by_clinic_name, name='update_clinic_room_by_clinic_name'),
    path('clinic-rooms/delete/', delete_clinic_room_by_clinic_name, name='delete_clinic_room_by_clinic_name'),

    path('beds/create', create_bed, name='create_bed'),
    path('beds/read', list_beds_by_room_number, name='get_beds_by_room_number')
]
