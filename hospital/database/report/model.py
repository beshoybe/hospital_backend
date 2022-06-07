from app import db
class Report(db.Model):
    __tablename__ = "report"
    id = db.Column(db.Integer, primary_key=True)
    added_to = db.Column(db.Integer,db.ForeignKey('user.id'))
    added_by = db.Column(db.Integer,db.ForeignKey('doctor.id'))
    medicines = db.Column(db.String(1000))
    report = db.Column(db.String(2000))
    report_datetime = db.Column(db.DateTime)
    type = db.Column(db.String(20))
    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,data):
        self.added_to = data['added_to']
        self.report = data['report']
        self.medicines = data['medicines']
        self.report_datetime = data['report_datetime']
        self.type = data['type']

    def __repr__(self):
        return '' %self.orders