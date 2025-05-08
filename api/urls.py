from django.urls import path
from .views import PacienteListCreateView,PacienteDetailView,DoctorListCreateView,DoctorDetailView,EspecialidadListCreateView,EspecialidadDetailView,CitaListCreateView,CitaDetailView,Especialidades_DoctoresListCreateView,Especialidades_DoctorDetailView

urlpatterns = [
     
     path('paciente/', PacienteListCreateView.as_view(), name='paciente-listar-crear'),
     path('paciente/<int:pk>/', PacienteDetailView.as_view(), name='paciente-editar-actualizar'),
     path('doctores/', DoctorListCreateView.as_view(), name='doctor-listar-crear'),
     path('doctores/<int:pk>/', DoctorDetailView.as_view(), name='doctor-editar-actualizar'),
     path('especialidad/', EspecialidadListCreateView.as_view(), name='especialidad-list-create'),
     path('especialidad/<int:pk>/', EspecialidadDetailView.as_view(), name='especialidad-editar-actualizar'),
     path('cita/', CitaListCreateView.as_view(), name='cita-list-create'),
     path('cita/<int:pk>/', CitaDetailView.as_view(), name='cita-editar-actualizar'),
]




