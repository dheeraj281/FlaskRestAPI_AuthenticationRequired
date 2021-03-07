from werkzeug.security import generate_password_hash,check_password_hash
from API_call import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password=password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Username {self.username}"

class Books(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    author = db.Column(db.String(64))
    language = db.Column(db.String(64))

    def __init__(self,title,author,language):
        self.title = title
        self.author = author
        self.language = language

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_row(self):
        db.session.delete(self)
        db.session.commit()


