from flask import Blueprint, flash, redirect,request, render_template
import os
import asyncio
from .models import EmpleadoDto
from database.repoEmpleado import setEmpleado

simple_page = Blueprint('simple_page', __name__,template_folder='../templates',url_prefix='/reg')
ALLOWED_EXTENSIONS = {'txt', 'mp4'}

@simple_page.route('/addEmpleado', methods=['GET', 'POST'])
async def register():
  form : EmpleadoDto = EmpleadoDto(request.form)
  try:
    if request.method == 'POST' and form.validate():
      #Guardar en la base de datos
      #asyncio.get_event_loop().run_until_complete(setEmplead

      #loop.run_until_complete(setEmpleado(form))
      await setEmpleado(form)

      if 'video' not in request.files:
        flash('No file part')
        return redirect(request.url)
      file = request.files['video']

      if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

      if file and allowed_file(file.filename):
        if not os.path.exists(f"videos/{form.nickname.data}"):
          print("No existe")
          os.mkdir(f"videos/{form.nickname.data}")
          print("Llega aqi")
        file.save(os.path.join( f"videos/{form.nickname.data}", f"{form.nickname.data}.mp4"))
        form = EmpleadoDto()
        return render_template('register.html', form=form,error="Listo!!")
    else:
      return render_template('register.html', form=form,error="")
      #return render_template('controluser.html')
  except Exception as e:
    print(e)
    return render_template('register.html', form=form, error=e)

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
