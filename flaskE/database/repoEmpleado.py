from .modeld import Empleado
from app.models import EmpleadoDto

async def setEmpleado(empleado:EmpleadoDto ):

  empleado = Empleado(
    nickname=empleado.nickname.data,
    correo=empleado.correo.data,
    nombre=empleado.nombre.data,
    nempleado=empleado.nEmpleado.data,
    telefono=empleado.telefono.data
  )
  await empleado.save()
  return True