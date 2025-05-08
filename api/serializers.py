from .models import paciente,doctores,especialidades,citas,doctores_especialidades
from rest_framework import serializers

#Paciente
class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model=paciente
        fields = ['id','nombre_paciente','apellido_paciente']



#Doctor
class DoctoresSerializer(serializers.ModelSerializer):
    class Meta:
        model=doctores
        fields = ['id','nombre_doctor','apellido_doctor']




#Especialidade
class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model=especialidades
        fields = ['id','lista_especialidades']



#Citas
class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model=citas
        fields = ['id','doctores','paciente','fecha_cita','motivo_cita']



#Tabla intermedia de doctores y especialidades
class Doctores_EspecialidadesSerializers(serializers.ModelSerializer):
    class Meta:
        model=doctores_especialidades
        fields= '__all__'


