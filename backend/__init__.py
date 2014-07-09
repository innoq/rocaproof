from flask import Flask, render_template


app = Flask(__name__)

TITLE = "ROCAproof"


@app.route("/")
def frontpage():
    return render_template("index.html", title=TITLE)
