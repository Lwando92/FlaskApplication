from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    physics = IntegerField('Physics',validators=[DataRequired()])
    maths = IntegerField('Maths', validators=[DataRequired()])
    chemistry = IntegerField('Chemistry', validators=[DataRequired()])
    submit = SubmitField('Submit')


# IntegerField('Telephone', [validators.NumberRange(min=0, max=10)])
