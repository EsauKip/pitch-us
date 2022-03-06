from flask import Flask
from app import views
from app import error

# Initializing application
app = Flask(__name__)
app.config['SECRET_KEY'] ='iamkip'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://moringa:kiprono12@localhost/pitches'

pitch=[
    {
        'author':'haveys',
        'title':'first post',
        'content': 'be careful!'   },
        {
            'author':'jim reeves',
            'title':'second post',
            'content': 'never ever give up'
        }
]
from app import views