from flask import Flask,request,render_template,flash, redirect, url_for, Request
import os
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf


from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired








app = Flask(__name__)

class Felis(FlaskForm):
  name = StringField(name='name')
  last  = FileField(name='last')


app.config['SECRET_KEY'] = 'tu_clave_secreta'

@app.route('/get_csrf_token', methods=['GET'])
def get_csrf_token():
    csrf_token = generate_csrf()
    return {'csrf_token': csrf_token}


@app.route('/<name>')
def hello(name):
  return f"<H1>Hello World! ,{name}</H1>"


@app.route('/', methods=['POST','GET'])
def index():
  if request.method == 'GET':
    return render_template('hello.html', msg = 'Hello World')



@app.route("/forma",methods=['POST','GET'])
def form():
  forsa = Felis(request.form)
  return forsa.last.data
  if request.method == 'POST' and forsa.validate():
    return {"msg":"Heeelo"}
  return {"ws":"sss"}



UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mp4'}


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/files', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        #format = Felis(request.form)

        if 'video' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['video']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "nuevo.jpg"))
            return redirect("/")
    return {"msg": "errror"}
