from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt
from task3 import app
 
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.CHAR(64), nullable=False)
    birthday = db.Column(db.DateTime)
    consent_person_data = db.Column(db.DateTime)

    @property
    def password(self):
        raise AttributeError('password not readable')
    
    @password.setter
    def password(self, password: str):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def check_password(self, password: str):
        return bcrypt.checkpw(password.encode(), self.password_hash)

    def __repr__(self):
        return f'{self.username} (birthday: {self.birthday}), e-mail: {self.email})'