from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, SubmitField, BooleanField, DateField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, EqualTo, Optional

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired("Please enter your username"), Length(5, 30)], id='username')
    password = PasswordField("Password", validators=[InputRequired("Please enter your password"), Length(6, 20)], id='password')
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")


class PersonForm(FlaskForm):
    p_name = StringField("Person name", validators=[InputRequired("Please enter author's name"), Length(1, 30, "Name can not be longer than %(max)d character")], id='person_name')
    p_surname = StringField("Person surname", validators=[InputRequired("Please enter author's surname"), Length(1, 30, "Surname can not be longer than %(max)d character")], id='person_surname')
    p_gender = SelectField("Person gender", choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Not specified')], validators=[InputRequired("A gender must be provided")], id='person_gender')
    p_dob = DateField("Person birth of date", validators=[Optional()], id='person_dob')
    p_nationality = StringField("Person nationality", validators=[Optional(), Length(1, 50, "Nationality length should be between %(min)d and %(max)d character")], id='person_nationality')



class AuthorForm(PersonForm):
    a_biography = TextAreaField("Author biography", validators=[Optional(), Length(1, 1000, "Author biography length should be between %(min)d and %(max)d character")], id='author_biography')
    submit = SubmitField("Add Author")

