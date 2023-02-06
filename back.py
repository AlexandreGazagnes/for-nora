import os, sys, logging


from src.back.app import create_app

BACK_DEBUG = True
BACK_PORT = 8080
BACK_HOST = "0.0.0.0"

if __name__ == "__main__":
    app = create_app()
    app.run(
        debug=BACK_DEBUG,
        port=BACK_PORT,
        host=BACK_HOST,
    )
