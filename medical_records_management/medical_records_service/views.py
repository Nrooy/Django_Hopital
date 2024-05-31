from rest_framework.views import APIView
from bson.objectid import ObjectId
from rest_framework.response import Response
from rest_framework import status

from .models import MedicalRecord, Prescription
from .serializers import MedicalRecordSerializer, PrescriptionSerializer
# Create your views here.

class MedicalRecordAPIView(APIView):
    def get(self, request):
        try:
            id_str = request.query_params.get("id")
            if id_str != '':
                try:
                    medical_record = MedicalRecord.objects.get(_id=ObjectId(id_str))
                    serializer = MedicalRecordSerializer(medical_record)
                    # Return serialized data with status code 200
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except MedicalRecord.DoesNotExist:
                    # If no record is found with the given ID
                    return Response({"error": "Medical record not found"}, status=status.HTTP_404_NOT_FOUND)
            else: 
                return Response({"error": "Medical record id not found"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({'message': 'HTTP_500_INTERNAL_SERVER_ERROR'},status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request, format=None):
        try:
            serializer = MedicalRecordSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'message': 'HTTP_500_INTERNAL_SERVER_ERROR'},status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class MedicalRecordListAPIView(APIView):
    def id_str(self, request):
        try:
            patient_id_str = request.query_params.get("id","")
            if patient_id_str != "": 
                patient_id = ObjectId(patient_id_str)
                medical_records = MedicalRecord.objects.filter(patient_id=patient_id)
                serializer = MedicalRecordSerializer(medical_records, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                medical_records = MedicalRecord.objects.all()
                serializer = MedicalRecordSerializer(medical_records, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'message': 'HTTP_500_INTERNAL_SERVER_ERROR'},status = status.HTTP_500_INTERNAL_SERVER_ERROR)


                