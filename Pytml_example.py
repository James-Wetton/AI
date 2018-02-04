from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Index page where user can make new doc."""
    return render_template("new.html", name="new_name")


@app.route("/new")
def new():
    return "this is different"


if __name__ == "__main__":
    app.run()
