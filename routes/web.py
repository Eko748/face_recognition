from flask import Flask
from controllers import LoginController, FaceRecognitionController

app = Flask(__name__, template_folder='../templates', static_folder='../static')
# To Do List
@app.route('/')
def wellcome():
    return 'Halo'

@app.route('/login', methods=('GET', 'POST'))
def logins():
    return LoginController.login()

@app.route('/person')
def persons():
    return FaceRecognitionController.person()

