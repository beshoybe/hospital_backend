from flask import jsonify, make_response, request
from flask_jwt_extended import get_jwt_identity
from flask_restful import Resource
from marshmallow import ValidationError
from pymysql import IntegrityError
from database.user.radiology.schema import UserRadiologySchema,UserRadiology
from resources.errors import *
from resources.jwt_func import jwt_needed
class AddRadiologyApi(Resource):
    @jwt_needed
    def post(self):
        try:
            data = request.get_json()
            id = get_jwt_identity()
            radiology_schema = UserRadiologySchema()
            radiology = radiology_schema.load(data)
            radiology = UserRadiology(radiology)
            radiology.added_by = id
            radiology.create()
            return make_response(jsonify({"message":'radiology Saved'}),200)
        except ValidationError:
            raise SchemaValidationError
        except IntegrityError as e:
           raise UserAlreadyExistError
        except Exception as e:
            raise e
class AddUserRadiologyApi(Resource):
    @jwt_needed
    def post(self):
        try:
            data = request.get_json()
            id = get_jwt_identity()
            radiology_schema = UserRadiologySchema()
            radiology = radiology_schema.load(data)
            radiology = UserRadiology(radiology)
            radiology.added_to = id
            radiology.create()
            return make_response(jsonify({"message":'radiology Saved'}),200)
        except ValidationError:
            raise SchemaValidationError
        except IntegrityError as e:
           raise UserAlreadyExistError
        except Exception as e:
            raise e




image_path = "static/images/"
class AddRadiologyImageApi(Resource):
    def post(self):
        try:
            id = request.form['id']
            radiology = UserRadiology.query.get(id)
            file_to_upload = request.files['file']
            ext = ext_check(file_to_upload.filename)
            if ext:
                path = image_path+'radiology/'+id+ext
                file_to_upload.save(path)
                radiology.photo = path
                radiology.create()
            return {'message':'image saved successfully'},200
        except Exception as e:
            raise e
allowed_ext = ['.png','.jpg','.gif','.webp','.jpeg']
def ext_check(img_name):
    for i in allowed_ext:
        if i in img_name:
            return i