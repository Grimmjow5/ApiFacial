from flask import Flask,request,render_template,flash
import os
from flask_wtf.csrf import generate_csrf

from app.routes import simple_page

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'
app.config['UPLOAD_FOLDER'] = "videos"
app.register_blueprint(simple_page)

@app.route('/get_csrf_token', methods=['GET'])
def get_csrf_token():
    csrf_token = generate_csrf()
    return {'csrf_token': csrf_token}



@app.route('/', methods=['POST','GET'])
def index():
  if request.method == 'GET':
    return render_template('hello.html', msg = 'Hello World')
