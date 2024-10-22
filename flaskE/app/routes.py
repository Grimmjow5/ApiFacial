from flask import Blueprint, flash, redirect,request, render_template
import os
from .models import EmpleadoDto, RegistrationForm


simple_page = Blueprint('simple_page', __name__,template_folder='../templates',url_prefix='/reg')

#UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'mp4'}



def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#@simple_page.route('/files', methods=['GET', 'POST'])
@simple_page.route("/addEmpleado",methods=['POST','GET'])
def upload_file():
  forma = EmpleadoDto(request.form)
  if request.method == 'POST':
    print(forma.validate())
    if forma.validate():
      print("Success")
    return {"msh" : forma.nickname.data}

  return render_template('controluser.html')



@simple_page.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        print("Success")
    #    user = User(form.username.data, form.email.data,
    #                 form.password.data)
    #    db_session.add(user)

        flash('Thanks for registering')
        return redirect("addEmpleado")
    return render_template('register.html', form=form)



'''
      if request.method == 'POST' and forma.validate():
        print("Success")

      if 'video' not in request.files:
          flash('No file part')
          return redirect(request.url)
      file = request.files['video']

      if file.filename == '':
          flash('No selected file')
          return redirect(request.url)

      if file and allowed_file(file.filename):
          file.save(os.path.join( 'uploads', f"{forma.username.data}.mp4"))
          return redirect(request.url)
  else:
    return render_template('controluser.html')

  return {"msg": "errror"}
'''