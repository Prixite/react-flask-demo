from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/profile")
def profile():
    return dict(
        name='Umair Khan',
        email='umair@example.com',
        country='Pakistan',
    )
