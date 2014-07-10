from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.widgets.core import Input, HTMLString
from wtforms.validators import DataRequired, Email


class SampleForm(Form):
    username = TextField("username")
    email = EmailField("e-mail", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
