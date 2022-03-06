from flask import render_template
from app import main
from flask_login import login_required,redirect,url_for,current_user
from ..models import User, Pitch, Category
from .forms import PitchForm


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    Category=Category.query_all()
    title='Pitch'
    return render_template('index.html',title=title,Category=Category)
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        newPitch = form.pitch_info.data
        #update pitch instance
        new_pitch = Pitch(pitch_title=title,
                          pitch_category=category,
                          pitch_itself=newPitch,
                          user=current_user)
        #save pitch
        new_pitch.save_pitch()
        return redirect(url_for('.index'))
    title = 'Add New pitch'
    return render_template('pitches.html', title=title, pitchesform=form)
