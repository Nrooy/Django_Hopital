"""Patient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from patient_service.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthinsurance/add/', HealthInsuranceCreateView.as_view(), name='healthinsurance-add'),
    path('healthinsurance/<pk>/edit/', HealthInsuranceUpdateView.as_view(), name='healthinsurance-edit'),
    path('healthinsurance/<pk>/delete/', HealthInsuranceDeleteView.as_view(), name='healthinsurance-delete'),
    path('patient/', PatientCreateView.as_view(), name='patient-create'),
    path('patient/<pk>/', PatientUpdateView.as_view(), name='patient-update'),
    path('patient/<pk>/delete/', PatientDeleteView.as_view(), name='patient-delete'),
    path('patient/<pk>/detail/', PatientDetailView.as_view(), name='patient-detail'),
    path('patients/', PatientListView.as_view(), name='patient-list'),
]

