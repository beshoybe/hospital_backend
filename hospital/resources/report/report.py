from datetime import datetime
from flask import jsonify, make_response, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from marshmallow import ValidationError
from pymysql import IntegrityError
from database.report.schema import ReportSchema
from database.report.model import Report
from resources.errors import *
from resources.jwt_func import jwt_needed
from flask_jwt_extended import get_jwt_identity
class AddReportApi(Resource):
    @jwt_needed
    def post(self):
        try:
            data = request.get_json()
            id = get_jwt_identity()
            report_schema = ReportSchema()
            report = report_schema.load(data)
            report = Report(report)
            report.added_by = id
            report.create()
            return make_response(jsonify({"message":'Report Saved'}),200)
        except ValidationError:
            raise SchemaValidationError
        except IntegrityError as e:
           raise UserAlreadyExistError
        except Exception as e:
            raise e
class AddUserReportApi(Resource):
    @jwt_needed
    def post(self):
        try:
            data = request.get_json()
            id = get_jwt_identity()
            report_schema = ReportSchema()
            report = report_schema.load(data)
            report = Report(report)
            report.added_to = id
            report.create()
            return make_response(jsonify({"message":'Report Saved'}),200)
        except ValidationError:
            raise SchemaValidationError
        except IntegrityError as e:
           raise UserAlreadyExistError
        except Exception as e:
            raise e