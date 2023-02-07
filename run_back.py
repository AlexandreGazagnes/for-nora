import os, sys, logging, json

from src.back.app import create_app


with open("./conf.back.json", "r") as f:
    data = json.load(f)

if __name__ == "__main__":
    app = create_app()
    # app.run(
    #     debug=eval(os.getenv("BACK_DEBUG")),
    #     port=int(os.getenv("BACK_PORT")),
    #     host=os.getenv("BACK_HOST"),
    # )

    app.run(
        debug=data.get("BACK_DEBUG"),
        port=data.get("BACK_PORT"),
        host=data.get("BACK_HOST"),
    )
