from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
  email = StringField('Enter your email address',validators=[Required(),Email()])
  username = StringField('Enter your username',validators=[Required()])
  password = PasswordField('Enter password',validators=[Required(),EqualTo('password_confirm',message='passwords must match')])
  password_confirm = PasswordField('Confirm Passwords',validators=[Required()])
  submit = SubmitField('Sign Up')
  
  def validate_email(self,data_field):
    if User.query.filter_by(email = data_field.data).first():
      raise ValidationError('There is an account with that email')
    
  def validate_username(self,data_field):
    if User.query.filter_by(username = data_field.data).first():
      raise ValidationError('Username is already taken')


class LoginForm(FlaskForm):
  username = StringField('Enter your username',validators=[Required()])
  password = PasswordField('Enter password',validators=[Required()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Login')