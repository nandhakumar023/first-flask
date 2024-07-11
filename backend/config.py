from flask import Flask
from flask_sqlalchemy import SQLAlchemy #acts as ORM object relational maping
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #cross origin requst (origin=domine) 

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODFICATIONS"] = False

db = SQLAlchemy(app)
