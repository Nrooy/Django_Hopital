from rest_framework import viewsets
from .models import Clinic, Bed, ClinicRoom
from .serializers import ClinicSerializer, BedSerializer, ClinicRoomSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class ClinicRoomViewSet(viewsets.ModelViewSet):
    queryset = ClinicRoom.objects.all()
    serializer_class = ClinicRoomSerializer


class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

@api_view(['POST'])
def create_clinic_room(request):
    clinic_name = request.data.get('clinic_name')

    try:
        clinic = Clinic.objects.get(name=clinic_name)
    except Clinic.DoesNotExist:
        return Response({"clinic": [f"Clinic with name '{clinic_name}' does not exist."]}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ClinicRoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['clinic'] = clinic
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_clinic_rooms_by_clinic_name(request):
    clinic_name = request.data.get('clinic_name', None)
    
    if not clinic_name:
        return Response({"detail": "Clinic name is required in the request body."}, status=400)
    
    try:
        clinic = Clinic.objects.get(name=clinic_name)
        clinic_rooms = ClinicRoom.objects.filter(clinic=clinic)
        serializer = ClinicRoomSerializer(clinic_rooms, many=True)
        return Response(serializer.data)
    
    except ObjectDoesNotExist:
        return Response({"detail": f"Clinic with name '{clinic_name}' does not exist."}, status=404)
    
@api_view(['PUT'])
def update_clinic_room_by_clinic_name(request, room_id):
    clinic_name = request.data.get('clinic_name')

    try:
        clinic = Clinic.objects.get(name=clinic_name)
    except Clinic.DoesNotExist:
        return Response({"clinic": [f"Clinic with name '{clinic_name}' does not exist."]}, status=status.HTTP_400_BAD_REQUEST)

    try:
        clinic_room = ClinicRoom.objects.get(id=room_id, clinic=clinic)
    except ClinicRoom.DoesNotExist:
        return Response({"detail": f"Clinic room with ID '{room_id}' does not exist for clinic '{clinic_name}'."}, status=status.HTTP_404_NOT_FOUND)

    serializer = ClinicRoomSerializer(clinic_room, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_clinic_room_by_clinic_name(request, room_id):
    clinic_name = request.data.get('clinic_name')

    try:
        clinic = Clinic.objects.get(name=clinic_name)
    except Clinic.DoesNotExist:
        return Response({"clinic": [f"Clinic with name '{clinic_name}' does not exist."]}, status=status.HTTP_400_BAD_REQUEST)

    try:
        clinic_room = ClinicRoom.objects.get(id=room_id, clinic=clinic)
    except ClinicRoom.DoesNotExist:
        return Response({"detail": f"Clinic room with ID '{room_id}' does not exist for clinic '{clinic_name}'."}, status=status.HTTP_404_NOT_FOUND)

    clinic_room.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_bed(request):
    room_number = request.data.get('room_number')

    try:
        clinic_room = ClinicRoom.objects.get(room_number=room_number)
    except ClinicRoom.DoesNotExist:
        return Response({"clinic_room": [f"Clinic room with room number '{room_number}' does not exist."]}, status=status.HTTP_400_BAD_REQUEST)

    serializer = BedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['clinic_room'] = clinic_room
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_beds_by_room_number(request):
    room_number = request.data.get('room_number', None)
    if not room_number:
        return Response({"detail": "Room number is required in the request body."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        clinic_room = ClinicRoom.objects.get(room_number=room_number)
    except ClinicRoom.DoesNotExist:
        return Response({"detail": f"Clinic room with room number '{room_number}' does not exist."}, status=status.HTTP_404_NOT_FOUND)

    beds = Bed.objects.filter(clinic_room=clinic_room)
    serializer = BedSerializer(beds, many=True)
    return Response(serializer.data)

