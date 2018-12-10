from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired("Please enter your username"), Length(5, 30)], id='username')
    password = PasswordField("Password", validators=[DataRequired("Please enter your password"), Length(6, 20)], id='password')
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")