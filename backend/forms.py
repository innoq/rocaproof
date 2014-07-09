from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email


class SampleForm(Form):
    username = TextField("username")
    email = TextField("e-mail", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
