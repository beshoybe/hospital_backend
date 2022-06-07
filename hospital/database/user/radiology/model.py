from app import db
class UserRadiology(db.Model):
    __tablename__ = "userradiology"
    id = db.Column(db.Integer, primary_key=True)
    added_to = db.Column(db.Integer,db.ForeignKey('user.id'))
    added_by = db.Column(db.Integer,db.ForeignKey('doctor.id'))
    photo = db.Column(db.String(150),default = '')
    report = db.Column(db.String(2000))
    type = db.Column(db.String(20))
    report_datetime = db.Column(db.DateTime)
    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,data):
        self.added_to = data['added_to']
        self.report = data['report']
        self.type = data['type']
        self.report_datetime=data['report_datetime']