from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, TextField
from wtforms.validators import DataRequired, ValidationError

from app.models import StudentDetail

class StudentDetailsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    roll_no = IntegerField('Roll Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_roll_no(self, roll_no):
        roll_no = str(roll_no.data)
        if len(roll_no) != 9:
            raise ValidationError('Invalid Roll Number')
        if StudentDetail.query.filter_by(roll_no=roll_no).first():
            raise ValidationError('Roll Number Already Exists.')

    def validate_name(self, name):
        if StudentDetail.query.filter_by(name=(name.data).strip()).first():
            raise ValidationError('Student Name Already Exists.')

class UpdateForm(FlaskForm):
    name = StringField('Name')
    roll_no = IntegerField('Roll Number')
    submit = SubmitField('Submit')

    def validate_roll_no(self, roll_no):
        roll_no = str(roll_no.data)
        if len(roll_no) != 9:
            raise ValidationError('Invalid Roll Number')

class SearchForm(FlaskForm):
    search = TextField('Search', id='searchlist')
    submit = SubmitField('Search')

    def validate_search(self, search):
        if not (StudentDetail.query.filter_by(name=(search.data).strip()).first() \
                or StudentDetail.query.filter_by(roll_no=(str(search.data)).strip()).first()):
            raise ValidationError("Student Doesn't Exist")

        
