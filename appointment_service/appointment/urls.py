from django.urls import path
from . import views 

urlpatterns = [
    path('', views.ListCreateAppointmentAPIView.as_view(), name='get_post_appointments'),
    path('<int:pk>/', views.RetrieveUpdateDestroyAppointmentAPIView.as_view(), name='get_delete_update_appointment'),
]