from marshmallow_sqlalchemy import SQLAlchemySchema
from database.doctor.doctor.model import Doctor
from marshmallow import fields
from app import db

class DoctorSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Doctor
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    password = fields.String(required=True)
    photo = fields.String()
    specialize = fields.String(required=True)
    price =  fields.Float(required=True)
    bio = fields.String()
