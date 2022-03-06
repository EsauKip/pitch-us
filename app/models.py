from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique=True,nullable=False)
    email = db.Column(db.String(255),unique = True,nullable=False) 
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")
    pitches=db.relationship('Pitch',backref='author',lazy=True)
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    def __repr__(self):
        return f'User {self.username},{self.email},{self.image_file}'



class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable=False)
    content = db.Column(db.text,nullable=False)
    votes = db.relationship('Vote', backref = 'pitches', lazy = "dynamic")
   
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()


    def get_pitches(id):
        pitches = Pitch.query.filter_by(category_id=id).all()
        return pitches

    def __repr__(self):
        return f'Pitch {self.title}'
class Comment(db.Model):

    __tablename__='Comments'
    id = db.Column(db.Integer, primary_key = True)
    feedback = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    

    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    # @classmethod
    # def get_comments(self, id):
    #     comment = Comments.query.order_by(Comments.time_posted.desc()).filter_by(pitches_id=id).all()
    #     return comment
    