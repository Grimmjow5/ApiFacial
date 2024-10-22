
from wtforms import StringField, validators, Form, FileField, PasswordField, BooleanField

class EmpleadoDto(Form):
  nickname = StringField('Username', [validators.Length(min=4, max=25)])
  nombre = StringField('Full name', [validators.Length(min=4, max=100)])
  correo = StringField('Email Address', [validators.Length(min=6, max=35)])
  nEmpleado =StringField('Number Employee', [validators.Length(min=6, max=35)])
  telefono =StringField('Telephone Number', [validators.Length(min=6, max=35)])

  video = FileField("Video",[validators.DataRequired()])



class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])