import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

secretKey = 'cbn'
host = 'localhost'
user = 'root'
database = 'face_db'

mydb = mysql.connector.connect(
    host= host,
    user= user,
    passwd="",
    database= database
)
mycursor = mydb.cursor()

db = SQLAlchemy(app)