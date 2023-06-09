import datetime as dt

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", current_time=dt.datetime.utcnow())


if __name__ == "__main__":
    app.run()
