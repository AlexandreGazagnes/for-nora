import os, sys, logging

from src.back.app import create_app


def main():
    """ """

    app = create_app()
    app.run(
        debug=os.getenv("BACK_DEBUG"),
        port=os.getenv("BACK_PORT"),
        host=os.getenv("BACK_HOST"),
    )


if __name__ == "__main__":
    main()
