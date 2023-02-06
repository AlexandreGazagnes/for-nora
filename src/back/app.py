# import pickle, os, sys, logging
import os, sys, logging
# import requests

# import pandas as pd
# import numpy as np

# from sklearn.model_selection import *
# from sklearn.compose import *
# from sklearn.pipeline import *
# from sklearn.impute import *
# from sklearn.preprocessing import *
# from sklearn.ensemble import *

# import pandas as pd
# import shap

from flask import Flask

# shap.initjs()


from src.back.routes import _get_explaination, _get_passenger, _get_prediction, _get_model_decision, _getids, _hello






def create_app():

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return _hello()


    @app.route("/getids")
    def getids():
        return _getids()


    @app.route("/get_passenger/<_id>")
    def get_passenger(_id):
        return _get_passenger(_id)


    @app.route("/get_prediction/<_id>")
    def get_prediction(_id):
        return _get_prediction(_id)


    @app.route("/model_decision")
    def get_model_decision():
        return _get_model_decision()


    @app.route("/get_explaination/<_id>")
    def get_explaination(_id):
        return _get_explaination(_id)

    return app

