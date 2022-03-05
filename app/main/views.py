from flask import render_template
from app import main
from flask_login import login_required


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')
@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch():
    return render_template('')
