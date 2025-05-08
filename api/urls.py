from django.urls import path
from .views import PacienteListCreateView,PacienteDetailView,DoctorListCreateView,DoctorDetailView,EspecialidadListCreateView,EspecialidadDetailView,CitaListCreateView,CitaDetailView,Especialidades_DoctoresListCreateView,Especialidades_DoctorDetailView

urlpatterns = [
     
     path('paciente/', PacienteListCreateView.as_view(), name='libros-listar-crear'),
     path('paciente/<int:pk>/', PacienteDetailView.as_view(), name='libros-editar-actualizar'),
     path('doctores/', DoctorListCreateView.as_view(), name='autores-listar-crear'),
     path('doctores/<int:pk>/', DoctorDetailView.as_view(), name='autores-editar-actualizar'),
     path('especialidad/', EspecialidadListCreateView.as_view(), name='categorias-list-create'),
     path('especialidad/<int:pk>/', EspecialidadDetailView.as_view(), name='categorias-editar-actualizar'),
     path('cita/', CitaListCreateView.as_view(), name='libros-categorias-list-create'),
     path('cita/<int:pk>/', CitaDetailView.as_view(), name='libros-categorias-editar-actualizar'),
]




