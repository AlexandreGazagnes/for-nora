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


def create_app(data: dict) -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def hello(data=data):
        return _hello(data=data)

    @app.route("/get_ids")
    def get_ids(data=data):
        return _get_ids(data=data)

    @app.route("/get_passenger/<_id>")
    def get_passenger(_id, data=data):
        return _get_passenger(_id, data=data)

    @app.route("/get_prediction/<_id>")
    def get_prediction(_id, data=data):
        return _get_prediction(_id, data=data)

    @app.route("/get_model_decision")
    def get_model_decision(data=data):
        return _get_model_decision(data=data)

    @app.route("/get_shap/<_id>")
    def get_shap(_id, data=data):
        return _get_shap(_id, data=data)

    return app
