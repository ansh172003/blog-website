from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField
from flask_wtf.file import FileField, FileAllowed
import imghdr

def allow_only_jpeg(form, field):
    if field.data:
        image_format = imghdr.what(field.data)
        if image_format != 'jpeg':
            field.data = None



class UserForm(FlaskForm):
    name = StringField("Enter your name", validators=[DataRequired()])
    username = StringField("Enter your username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    about_author = TextAreaField("About Author", widget=TextArea())   
    profile_pic = FileField("Profile Picture", validators=[FileAllowed(['jpg', 'jpeg'], 'Only JPEG images are allowed.'), allow_only_jpeg])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('password2', message="Passwords must match")])
    password2 = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class BlogForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = CKEditorField("Content", validators=[DataRequired()])
    slug = StringField("Slug", validators=[DataRequired()])
    submit = SubmitField("Submit", validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")
