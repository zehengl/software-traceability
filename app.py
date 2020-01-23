from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from whitenoise import WhiteNoise

app = Flask(__name__)
Bootstrap(app)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="datasets", prefix="datasets")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True


@app.route("/", methods=["get"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
