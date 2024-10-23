
from wtforms import StringField, validators, Form, FileField, PasswordField, BooleanField,IntegerField

class EmpleadoDto(Form):
  nickname = StringField('Username', [validators.Length(min=4, max=25)])
  nombre = StringField('Nombre Completo', [validators.Length(min=4, max=100)])
  correo = StringField('Correo', [validators.Length(min=6, max=35)])

  nEmpleado =IntegerField('Número de Empleado')
  telefono =IntegerField('Número de Telefono')

  video = FileField('Image File')



class RegistrationForm(Form):
    username = StringField('Nickname', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])