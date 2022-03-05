from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique=True,nullable=False)
    email = db.Column(db.String(255),unique = True,nullable=False) 
    image_file = db.Column(db.String(20),nullable=False,default='default.jpeg')
    password = db.Column(db.String(60),nullable=False)
    pitches_id =db.Column(db.Integer,db.ForeignKey('pitche.id'))
    
    def __repr__(self):
        return f'User {self.username},{self.email},{self.image_file}'
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String)
    users = db.relationship('User',backref = 'pitches',lazy="dynamic")

    # category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    def __repr__(self):
        return f'User {self.name}'