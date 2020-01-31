from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from whitenoise import WhiteNoise

from datasets import CM1, CM1_Sub, GanttProject, MODIS, Pine, WorldVistA

app = Flask(__name__)
Bootstrap(app)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="datasets", prefix="datasets")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True


@app.route("/", methods=["get"])
def index():
    return render_template("index.html")


@app.route("/browse", methods=["get"])
def browse():
    return render_template(
        "browse.html",
        datasets=[CM1(), CM1_Sub(), GanttProject(), MODIS(), Pine(), WorldVistA()],
    )


@app.route("/baseline", methods=["get"])
def baseline():
    return render_template("baseline.html")


if __name__ == "__main__":
    app.run(debug=True)
