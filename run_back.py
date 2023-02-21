import os, sys, logging, json

from src.back.app import create_app


with open("./conf.back.json", "r") as f:
    data = json.load(f)


def main(data):
    """ """

    # create app
    app = create_app(data)

    # run
    app.run(
        debug=data.get("BACK_DEBUG", True),
        port=data.get("BACK_PORT", 8080),
        host=data.get("BACK_HOST", "0.0.0.0"),
    )


if __name__ == "__main__":
    main(data)
