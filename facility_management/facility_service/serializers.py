from rest_framework import serializers
from .models import Clinic, Bed, ClinicRoom

class ClinicRoomSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)

    class Meta:
        model = ClinicRoom
        fields = ['id', 'room_number']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if '_id' in ret:
            ret['id'] = str(ret['_id'])
            del ret['_id']
        return ret

class BedSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)

    class Meta:
        model = Bed
        fields = ['id', 'number', 'is_occupied']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if '_id' in ret:
            ret['id'] = str(ret['_id'])
            del ret['_id']
        return ret

class ClinicSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='_id', read_only=True)
    clinic_rooms = ClinicRoomSerializer(many=True, read_only=True)

    class Meta:
        model = Clinic
        fields = ['id', 'name', 'description', 'clinic_rooms']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if '_id' in ret:
            ret['id'] = str(ret['_id'])
            del ret['_id']
        return ret
