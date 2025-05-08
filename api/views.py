from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import paciente,doctores,especialidades,citas,doctores_especialidades
from .serializers import PacientesSerializer,DoctoresSerializer,EspecialidadesSerializer,CitasSerializer,Doctores_EspecialidadesSerializers
# Create your views here.

#Pacientes
class PacienteListCreateView(ListCreateAPIView):
    queryset =paciente.objects.all()
    serializer_class =PacientesSerializer

class PacienteDetailView(RetrieveUpdateDestroyAPIView):
    queryset =paciente.objects.all()
    serializer_class =PacientesSerializer


#Doctores
class DoctorListCreateView (ListCreateAPIView):
      queryset =doctores.objects.all()
      serializer_class =DoctoresSerializer

class DoctorDetailView(RetrieveUpdateDestroyAPIView):
      queryset =doctores.objects.all()
      serializer_class =DoctoresSerializer

#Especialidades
class EspecialidadListCreateView(ListCreateAPIView):
    queryset =especialidades.objects.all()
    serializer_class =EspecialidadesSerializer

class EspecialidadDetailView(RetrieveUpdateDestroyAPIView):
    queryset =especialidades.objects.all()
    serializer_class =EspecialidadesSerializer


#Citas
class CitaListCreateView(ListCreateAPIView):
    queryset =citas.objects.all()
    serializer_class =CitasSerializer

class CitaDetailView(RetrieveUpdateDestroyAPIView):
    queryset =citas.objects.all()
    serializer_class =CitasSerializer


#Doctor y sus especialidades
class Especialidades_DoctoresListCreateView(ListCreateAPIView):
    queryset =doctores_especialidades.objects.all()
    serializer_class =DoctoresSerializer

class Especialidades_DoctorDetailView(RetrieveUpdateDestroyAPIView):
    queryset =doctores_especialidades.objects.all()
    serializer_class =Doctores_EspecialidadesSerializers