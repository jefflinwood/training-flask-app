from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello</h1>"

@app.get("/cats")
def cats():
    all_cats = get_cats()
    return { "cats": all_cats }

def get_cats():
    return ["Tabby", "Tuxedo Cat", "Norwegian Forest Cats"]