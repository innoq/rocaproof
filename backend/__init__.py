from time import sleep
from collections import defaultdict

from flask import (Flask, flash, get_flashed_messages, render_template, url_for,
        request)
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
            flash("submitted data contains errors", "_error")

    return render("index.html", form=form,
            target=url_for("frontpage", **request.args))


def render(template, **kwargs):
    messages = { "global": [], "local": [] } # TODO: document
    for category, message in get_flashed_messages(with_categories=True):
        scope = "global"
        if category.startswith("_"):
            scope = "local"
            category = category[1:]
        messages[scope].append((category, message))

    delay = request.method == "POST" and request.args.get("delay") # TODO: document
    if delay:
        sleep(int(delay) / 10.0)
    return render_template(template, title=TITLE, messages=messages, **kwargs)
