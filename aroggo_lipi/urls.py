"""aroggo_lipi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from doctors import views as doctor_views
from patients import views as patients_views
from healthcare import views as healthcare_views

from django.conf.urls.static import static
from  django.views.static import serve
from  django.conf import settings

basePathString="aroggoLipi/"

urlpatterns = [
    path(basePathString+'admin/', admin.site.urls, name='adminPanel'),
    path(basePathString+'', patients_views.userLoginPage, name='userLoginPage'),
    path(basePathString+'userLoginProcess/', patients_views.userLoginProcess,
         name='userLoginProcess'),
    path(basePathString+'userRegisterPage/', patients_views.userRegisterPage,
         name='userRegisterPage'),
    path(basePathString+'userRegisterProcess/', patients_views.userRegisterProcess,
         name='userRegisterProcess'),
    path(basePathString+'doctors/', doctor_views.docLoginPage, name='docLoginPage'),
    path(basePathString+'docLoginProcess/', doctor_views.docLoginProcess, name='docLoginProcess'),
    path(basePathString+'docRegister/', doctor_views.docRegisterPage, name='docRegisterPage'),
    path(basePathString+'docRegisterProcess/', doctor_views.docRegisterProcess,
         name='docRegisterProcess'),

    path(basePathString+'healthcare/', healthcare_views.healthcareLoginPage,
         name='healthcareLoginPage'),
    path(basePathString+'healthcareLoginProcess/', healthcare_views.healthcareLoginProcess,
         name='healthcareLoginProcess'),
    path(basePathString+'panelRequest/',
         healthcare_views.panelRequest, name='panelRequest'),

    path(basePathString+'patientSelectProcess/',
         doctor_views.patientSelectProcess, name='patientSelectProcess'),


    path(basePathString+'savePatientStatus/',
         doctor_views.savePatientStatus, name='savePatientStatus'),
    path(basePathString+'deletePatientStatus/',
         doctor_views.deletePatientStatus, name='deletePatientStatus'),
    path(basePathString+'editPatientStatus/',
         doctor_views.editPatientStatus, name='editPatientStatus'),

    path(basePathString+'savePatientComplain/',
         doctor_views.savePatientComplain, name='savePatientComplain'),
    path(basePathString+'deletePatientComplain/',
         doctor_views.deletePatientComplain, name='deletePatientComplain'),
    path(basePathString+'editPatientComplain/',
         doctor_views.editPatientComplain, name='editPatientComplain'),


    path(basePathString+'savePatientDiagnosis/',
         doctor_views.savePatientDiagnosis, name='savePatientDiagnosis'),
    path(basePathString+'deletePatientDiagnosis/',
         doctor_views.deletePatientDiagnosis, name='deletePatientDiagnosis'),
    path(basePathString+'editPatientDiagnosis/',
         doctor_views.editPatientDiagnosis, name='editPatientDiagnosis'),



    path(basePathString+'savePatientTest/',
         doctor_views.savePatientTest, name='savePatientTest'),
    path(basePathString+'deletePatientTest/',
         doctor_views.deletePatientTest, name='deletePatientTest'),
    path(basePathString+'editPatientTest/',
         doctor_views.editPatientTest, name='editPatientTest'),

    path(basePathString+'savePatientInstruction/',
         doctor_views.savePatientInstruction, name='savePatientInstruction'),
    path(basePathString+'deletePatientInstruction/',
         doctor_views.deletePatientInstruction, name='deletePatientInstruction'),
    path(basePathString+'editPatientInstruction/',
         doctor_views.editPatientInstruction, name='editPatientInstruction'),

    path(basePathString+'savePatientMedicine/',
         doctor_views.savePatientMedicine, name='savePatientMedicine'),
    path(basePathString+'deletePatientMedicine/',
         doctor_views.deletePatientMedicine, name='deletePatientMedicine'),
    path(basePathString+'editPatientMedicine/',
         doctor_views.editPatientMedicine, name='editPatientMedicine'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
