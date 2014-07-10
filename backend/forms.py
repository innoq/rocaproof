from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.widgets.core import Input, HTMLString
from wtforms.validators import DataRequired, Email


# monkey-patching WTForms `Input` for inferred `required` attribute -- XXX: temporary workaround, hacky and brittle
_render = Input.__call__
def render(self, field, **kwargs):
    html = _render(self, field, **kwargs)
    if not field.flags.required:
        return html
    if not html[-1] == ">":
        raise RuntimeError("HTML augmentation failed")
    return HTMLString("%s required>" % html[:-1])
Input.__call__ = render


class SampleForm(Form):
    username = TextField("username")
    email = EmailField("e-mail", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
