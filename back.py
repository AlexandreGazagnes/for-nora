from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/getids")
def getids():
    ids = [1, 2, 3]
    return str(ids)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
