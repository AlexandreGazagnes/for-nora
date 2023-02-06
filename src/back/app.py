"""
App file with flask create function
"""

import os, sys, logging

from flask import Flask

from src.back.routes import (
    _hello,
    _get_ids,
    _get_passenger,
    _get_prediction,
    _get_model_decision,
    _get_shap,
)


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return _hello()

    @app.route("/get_ids")
    def get_ids():
        return _get_ids()

    @app.route("/get_passenger/<_id>")
    def get_passenger(_id):
        return _get_passenger(_id)

    @app.route("/get_prediction/<_id>")
    def get_prediction(_id):
        return _get_prediction(_id)

    @app.route("/get_model_decision")
    def get_model_decision():
        return _get_model_decision()

    @app.route("/get_shap/<_id>")
    def get_shap(_id):
        return _get_shap(_id)

    return app
