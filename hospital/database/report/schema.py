from marshmallow_sqlalchemy import SQLAlchemySchema
from database.radiology.model import Radiology
from marshmallow import fields
from app import db

class ReportSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        model = Radiology
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    added_to = fields.String()
    added_by = fields.String()
    medicines = fields.String()
    report = fields.String()
    report_datetime = fields.DateTime()
    type = fields.String()
