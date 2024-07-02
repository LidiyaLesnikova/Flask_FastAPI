from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

class RegisterForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    birthday = DateField('Birthday', validators=[DataRequired()])
    consent_person_data = BooleanField('Consent to the processing of personal data')
    password = PasswordField('Password', 
                             validators=[DataRequired(),
                                         Length(min=8, message='пароль должен быть не менее 8 символов'),
                                         Regexp("^.*(?=.*\d)(?=.*[a-zA-Z]).*$", message='пароль должен включать хотя бы одну букву (en) и одну цифру')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
