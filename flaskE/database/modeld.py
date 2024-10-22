from tortoise.models import Model
from tortoise import fields

class Empleado(Model):
  id = fields.IntField(primary_key=True)
  nickname = fields.CharField(max_length=30)
  nombre = fields.CharField(max_length=60)
  nEmpleado = fields.IntField()
  correo = fields.CharField(max_length=60)
  telefono = fields.IntField()