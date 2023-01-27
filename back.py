import pickle, os, sys, logging
import requests

import pandas as pd
import numpy as np

from sklearn.model_selection import *
from sklearn.compose import *
from sklearn.pipeline import *
from sklearn.impute import *
from sklearn.preprocessing import *
from sklearn.ensemble import *

import shap

from flask import Flask


df = pd.read_csv("./data/cleaned/df_train.csv")


passengers_id_list = list(df.PassengerId.values)


def extract_vect(PassengerId, _df):
    """extract from a df"""

    X = _df.loc[_df.PassengerId == PassengerId].copy()
    assert len(X) == 1

    Passenger_id = X.PassengerId[0]
    Survived = X.Survived[0]
    X = X.drop(columns=["PassengerId", "Survived"])
    ser = X.iloc[0].to_dict()

    return ser, Passenger_id, Survived


with open("./models/model.pk", "rb") as f:
    pk = f.read()
    model = pickle.loads(pk)


with open("./explainers/shap.pk", "rb") as f:
    pk = f.read()
    explainer = pickle.loads(pk)


app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Hello, World!</p>"


@app.route("/getids")
def getids():

    li = passengers_id_list[:30]

    return str(li)


@app.route("/get_passenger/<id>")
def get_passenger(id):

    dd, _id, _target = extract_vect(id, df)

    return dd


@app.route("/predict/<id>")
def predict(id):

    dd, _id, _target = extract_vect(id, df)
    # ans = model.predict(pd.Series(dd))
    prob = model.predict_proba(pd.Series(dd))

    return str(prob)


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
