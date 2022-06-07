from marshmallow_sqlalchemy import SQLAlchemySchema
from database.user.radiology.model import UserRadiology
from marshmallow import fields
from app import db

class UserRadiologySchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = UserRadiology
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    added_to = fields.String()
    added_by =fields.String()
    photo = fields.String()
    type = fields.String()
    report = fields.String()
    report_datetime = fields.DateTime()
