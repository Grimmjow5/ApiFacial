from flask import Blueprint, flash, redirect,request, render_template
import os
from .models import EmpleadoDto, RegistrationForm
import asyncio

from database.repoEmpleado import setEmpleado


simple_page = Blueprint('simple_page', __name__,template_folder='../templates',url_prefix='/reg')

#UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'mp4'}



def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#@simple_page.route('/files', methods=['GET', 'POST'])
@simple_page.route("/register",methods=['POST','GET'])
def upload_file():
  forma = EmpleadoDto(request.form)
  if request.method == 'POST':
    print(forma.validate())
    if forma.validate():
      print("Success")

    return render_template('register.html', form=forma)

  return render_template('controluser.html')



@simple_page.route('/addEmpleado', methods=['GET', 'POST'])
async def register():
  form : EmpleadoDto = EmpleadoDto(request.form)
  try:
    if request.method == 'POST' and form.validate():
      #Guardar en la base de datos
      asyncio.run(setEmpleado(form))
      if  save == False:
        raise Exception("No se guardo")

      if 'video' not in request.files:
        flash('No file part')
        print("No file part se redirecciona")
        return redirect(request.url)
      file = request.files['video']

      if file.filename == '':
        flash('No selected file')
        print("No selected file se redirecciona")
        return redirect(request.url)

      if file and allowed_file(file.filename):
        print("File se guarda")
        print(f"videos/{form.nickname.data}")
        if not os.path.exists(f"videos/{form.nickname.data}"):
          print("No existe")
          os.mkdir(f"videos/{form.nickname.data}")
          print("Llega aqi")
        file.save(os.path.join( f"videos/{form.nickname.data}", f"{form.nickname.data}.mp4"))

        return render_template('register.html', form=form,error="Listo!!")
    else:
      return render_template('register.html', form=form,error="")
      #return render_template('controluser.html')
  except Exception as e:
    print(e)
    return render_template('register.html', form=form, error=e)
