from django.db import models

# Create your models here.

'''Tabla paciente'''
class paciente (models.Model):
    nombre_paciente = models.CharField(max_length=40,null=False)
    apellido_paciente = models.CharField(max_length=40,null=False)
    edad_paciente = models.CharField(max_length=10, null=False)
    direccion = models.CharField(max_length=50,null=False)
    correo = models.CharField(max_length=50,unique=True,null=False)


'''Tabla doctores'''
class doctores (models.Model):
    nombre_doctor = models.CharField(max_length=40,null=False)
    apellido_doctor = models.CharField(max_length=40,null=False)
    años_experiencia = models.PositiveIntegerField()


'''Tabla especialidades'''
class especialidades (models.Model):
    lista_especialidades = models.CharField(max_length=40, null=False, unique=True)
  

'''Tabla citas'''
class citas (models.Model):
    doctores = models.ForeignKey(doctores,on_delete=models.CASCADE,related_name='citas')
    paciente = models.ForeignKey(paciente,on_delete=models.CASCADE,related_name='citas')
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)

'''Tabla intermedia de doctores y especialidades'''
class doctores_especialidades (models.Model):
    doctores = models.ForeignKey(doctores,on_delete=models.CASCADE,related_name='doctores_especialidades')
    paciente = models.ForeignKey(paciente,on_delete=models.CASCADE,related_name='doctores_especialidades')
    