from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique=True,nullable=False)
    email = db.Column(db.String(255),unique = True,nullable=False) 
    image_file = db.Column(db.String(20),nullable=False,default='default.jpeg')
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