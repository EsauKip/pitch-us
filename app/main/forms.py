from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField,RadioField,StringField,SelectField
from wtforms.validators import DataRequired





class PitchForm(FlaskForm):
    
    title = StringField('Pitch title',validators=[DataRequired()])
    category = SelectField("Choose Category",choices=[('tech','tech'),('science','science'),('politics','politics')])
    pitch_info = TextAreaField('Your Pitch',validators=[DataRequired()])
    submit = SubmitField('Submit')

#Comment Form
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField()
    vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])

#categoryForm
class CategoryForm(FlaskForm):
    name = TextAreaField('Category')
    submit = SubmitField()
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')    