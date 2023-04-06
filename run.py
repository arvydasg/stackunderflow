from flask import Flask

app = Flask(__name__)


@app.route("/")
def route_index():
    return "<h1>Cia bus geriausias mano sukurtas flask projektas!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
