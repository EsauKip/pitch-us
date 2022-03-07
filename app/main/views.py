from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm,CommentForm, UpdateProfile
from ..models import User,Pitch,Comments
from flask_login import login_required,current_user
from .. import db,photos

# Views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    all_pitches=Pitch.query.order_by('id').all()
    print(all_pitches)
    title='Pitches App'
    return render_template('index.html',title=title)
# @main.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     Category=Category.query_all()
#     title='Pitch'
#     return render_template('index.html',title=title,Category=Category)
@main.route('/pitch/newpitch', methods=['POST', 'GET'])    
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
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/category/tech')
def tech():
    '''
    view function to display sports pitches
    '''
    pitches=Pitch.get_pitches('tech')
    tech_title ='tech Pitches'
    return render_template('pitches/tech.html',title=tech_title,tech_pitch=pitches)
@main.route('/category/sciences')
def sciences():
    '''
    view function to display business pitches
    '''
    pitches=Pitch.get_pitches('sciences')
    sciences_title='sciences Pitches'
    return render_template('pitches/sciences.html',title=sciences_title, sciences_pitch=pitches)
@main.route('/category/politics')
def politics():
    '''
    view function to display business pitches
    '''
    pitches=Pitch.get_pitches('politics')
    politics_title = 'Politics Pitches'
    return render_template('pitches/politics.html',title=politics_title,politics_pitch=pitches)
