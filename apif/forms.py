from django.forms import ModelForm
from django import forms
from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['username', 'password', 'nombre', 'correo', 'nEmpleado']


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()