from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email

class UserPhoneNumber(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    confirm_phone_number = StringField('Confirm Phone Number', validators=[DataRequired(), EqualTo()])
    submit = SubmitField()