from time import sleep

from flask import Flask, flash, render_template, url_for, request
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
            flash("submitted data contains errors", "error")

    return render("index.html", form=form,
            target=url_for("frontpage", **request.args))


def render(template, **kwargs):
    delay = request.method == "POST" and request.args.get("delay") # TODO: document
    if delay:
        sleep(int(delay) / 10.0)
    return render_template(template, title=TITLE, **kwargs)
