import datetime
from flask import jsonify, make_response, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from marshmallow import ValidationError
from pymysql import IntegrityError
from database.user.schema import UserSchema
from database.user.model import User
from resources.errors import *
class UserSignupApi(Resource):
    def post(self):
        try:
            data = request.get_json()
            user_schema = UserSchema()
            user = user_schema.load(data)
            user = User(user)
            user.hash_password()
            user.create()
            return make_response(jsonify({"message":'User signup succesfully'}),200)
        except ValidationError:
            raise SchemaValidationError
        except IntegrityError as e:
           raise UserAlreadyExistError
        except Exception as e:
            raise e
class UserLoginApi(Resource):
    def post(self):
        try:
            data = request.get_json()
            if ('email' not in data) | ('password' not in data):
                raise ValidationError
            user =  User.query.filter(User.email==data['email']).first()
            if not user:
                raise UserNotFoundError
            authorized = user.check_password(data['password'])
            if not authorized:
                raise UserNotAuthorizedError
            expires = datetime.timedelta(days=1000)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            user_schema = UserSchema(only=('name','email','id'))
            user_schema = user_schema.dump(user)
            user_schema['token']= access_token
            return make_response({'message':'Login Succesfully','data':user_schema},200)
        except Exception as e:
            raise e