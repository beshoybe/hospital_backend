import datetime
from flask import jsonify, make_response, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from marshmallow import ValidationError
from pymysql import IntegrityError
from database.doctor.doctor.model import Doctor
from database.doctor.doctor.schema import DoctorSchema
from resources.errors import *
class DoctorSignupApi(Resource):
    def post(self):
        try:
            data = request.get_json()
            doctor_schema = DoctorSchema()
            doctor = doctor_schema.load(data)
            doctor = Doctor(doctor)
            doctor.hash_password()
            doctor.create()
            return make_response(jsonify({"message":'doctor signup succesfully'}),200)
        except ValidationError:
            raise SchemaValidationError
        except IntegrityError as e:
           raise UserAlreadyExistError
        except Exception as e:
            raise e
class DoctorLoginApi(Resource):
    def post(self):
        try:
            data = request.get_json()
            if ('id' not in data) | ('password' not in data):
                raise ValidationError
            doctor =  Doctor.query.filter(Doctor.email==data['id']).first()
            if not doctor:
                raise UserNotFoundError
            authorized = doctor.check_password(data['password'])
            if not authorized:
                raise UserNotAuthorizedError
            expires = datetime.timedelta(days=1000)
            access_token = create_access_token(identity=str(doctor.id), expires_delta=expires)
            doctor_schema = DoctorSchema(only=('name','id'))
            doctor_schema = doctor_schema.dump(doctor)
            doctor_schema['token']= access_token
            return make_response({'message':'Login Succesfully','data':doctor_schema},200)
        except Exception as e:
            raise e