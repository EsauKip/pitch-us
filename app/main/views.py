from flask import render_template
from app import main
from flask_login import login_required,redirect,url_for,current_user,request
from ..models import User, Pitch, Category
from .forms import PitchForm
from .forms import UpdateProfile,abort
from .. import db,photos


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
# @main.route('/categories/view_pitch/<int:id>', methods=['GET', 'POST'])
# @login_required
# def view_pitch(id):
#     '''
#     Function the returns a single pitch for comment to be added
#     '''

#     print(id)
#     pitches = Pitch.query.get(id)

#     if pitches is None:
#         abort(404)
    
#     comment = Comments.get_comments(id)
#     return render_template('pitch.html', pitches=pitches, comment=comment, category_id=id)
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
