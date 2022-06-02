from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from resources.errors import errors
app = Flask(__name__)
os.environ['ENV_FILE_LOCATION']='./.env'
app.config.from_envvar('ENV_FILE_LOCATION')
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://hospital:12345678@localhost:3306/hospital'
db = SQLAlchemy(app,session_options={"autoflush": False})
api = Api(app,errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app) 
from resources.routes import initialize_routes
initialize_routes(api)
db.create_all()
