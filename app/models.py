from . import db
from flask_login import UserMixin
from . import login_manager



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique=True,nullable=False)
    email = db.Column(db.String(255),unique = True,nullable=False) 
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    password = db.Column(db.String(60),nullable=False)
    pitches=db.relationship('Pitch',backref='author',lazy=True)
    
    def __repr__(self):
        return f'User {self.username},{self.email},{self.image_file}'
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable=False)
    content = db.Column(db.text,nullable=False)
    # users = db.relationship('User',backref = 'pitches',lazy="dynamic")

    # category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    def __repr__(self):
        return f'Pitch {self.title}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))