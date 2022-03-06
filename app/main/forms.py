from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField,RadioField
from wtforms.validators import Required




#Pitch Form
class PitchForm(FlaskForm):
    content = TextAreaField('Post Your Pitch')
    submit = SubmitField('Submit Pitch')

#Comment Form
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField()
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])

#categoryForm
class CategoryForm(FlaskForm):
    name = TextAreaField('Category')
    submit = SubmitField()
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')    