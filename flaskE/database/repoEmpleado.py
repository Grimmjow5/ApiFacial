from .modeld import Empleado
from app.models import EmpleadoDto
from tortoise import Tortoise

async def setEmpleado(empleado:EmpleadoDto ):
  try:
    emplead = Empleado(
      nickname=empleado.nickname.data,
      correo=empleado.correo.data,
      nombre=empleado.nombre.data,
      nempleado=empleado.nEmpleado.data,
      telefono=empleado.telefono.data
    )
    await emplead.save()
    await Tortoise.close_connections()
  except Exception as e:
    print(e)
