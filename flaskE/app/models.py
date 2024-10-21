from tortoise.models import Model
from tortoise import fields


from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired




class Felis(FlaskForm):
  name = StringField('name',validators=[DataRequired()])
  photo = FileField(validators=[FileRequired()])


'''
class Empleados(Model):
  id = fields.IntField(primary_key=True)
  name = fields.TextField()
'''
