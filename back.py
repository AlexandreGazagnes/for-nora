from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/getids")
def getids():

    ids = [
        1234,
        2345,
        3456,
    ]
    return str(ids)


@app.route("/predict/<id>")
def predict(id):

    id = int(id)
    dd = {
        1234: 1,
        2345: 0,
        3456: 1,
    }

    return str(dd[id])


if __name__ == "__main__":
    app.run(debug=True, port=8080)
