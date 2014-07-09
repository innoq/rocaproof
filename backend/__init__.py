from flask import Flask, flash, render_template
from .forms import SampleForm


app = Flask(__name__)

TITLE = "ROCAproof"


@app.route("/", methods=("GET", "POST"))
def frontpage():
    form = SampleForm()
    if form.is_submitted():
        if form.validate():
            flash("data submitted successfully")
        else:
            flash("submitted data contains errors")
    return render_template("index.html", title=TITLE, form=form)
