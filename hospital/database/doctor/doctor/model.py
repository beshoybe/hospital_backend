from app import db
from sqlalchemy.orm import relationship
from flask_bcrypt import generate_password_hash, check_password_hash
class Doctor(db.Model):
    __tablename__ = "doctor"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String(100))
    photo = db.Column(db.String(150),default = '')
    specialize = db.Column(db.String(150),default = '')
    bio = db.Column(db.String(2000),default = '')
    price =  db.Column(db.Float)
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,data):
        self.name = data['name']
        self.password = data['password']
        self.price = data['price']
        self.specialize = data['specialize']
        self.bio = data['bio']
        