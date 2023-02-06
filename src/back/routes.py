"""
Routes for flask app
"""

import os, sys, logging

import pandas as pd

# from flask import jsonify

from src.back.data import *
from src.back.pks import *


def _hello():
    """ """
    data = {"msg": "<p>Hello, World!</p>"}

    assert isinstance(data, dict)
    return str(data)


def _get_ids(n=30):
    """ """

    li = get_passenger_id(os.getenv("DATA_FILE"))
    logging.info(li)

    data = {"id_list": li[:n]}

    assert isinstance(data, dict)
    return str(data)


def _get_passenger(_id):
    """ """

    df = get_df(os.getenv("DATA_FILE"))
    data, _id, _target = extract_vect(_id, df)

    assert isinstance(data, dict)
    return str(data)


def _get_prediction(_id):
    """ """

    # extract
    df = get_df(os.getenv("DATA_FILE"))
    dd, _id, _target = extract_vect(_id, df)

    # build object predictable
    logging.info(dd)
    ser = pd.Series(dd)

    logging.info(ser)
    local_df = pd.DataFrame([ser])

    # pred and proba
    model = read_pk(os.getenv("MODEL_FILE"))
    pred = model.predict(local_df)[0]
    proba = model.predict_proba(local_df)[0]

    # ans
    data = {"pred": pred, "proba": proba.tolist()}
    logging.info(data)

    assert isinstance(data, dict)
    return str(data)


def _get_model_decision():
    """ """

    df = get_df(os.getenv("DATA_FILE"))
    model = read_pk(os.getenv("MODEL_FILE"))

    data = {
        k: v.round(2) for v, k in zip(model.feature_importances_, model.feature_names_in_)
    }

    assert isinstance(data, dict)
    return str(data)


def _get_shap(_id):
    """ """

    df = get_df(os.getenv("DATA_FILE"))
    dd, _id, _target = extract_vect(_id, df)

    explainer = read_pk(os.getenv("SHAP_FILE"))

    shap_values = explainer.shap_values(pd.DataFrame([dd]))
    shap_false = shap_values[0]
    shap_true = shap_values[1]

    cols = pd.DataFrame([dd]).columns

    # true / false
    shap_true = (
        pd.DataFrame(shap_true, columns=cols)
        .iloc[0]
        .sort_values(ascending=False)
        .head(5)
        .round(2)
        .to_dict()
    )
    shap_false = (
        pd.DataFrame(shap_false, columns=cols)
        .iloc[0]
        .sort_values(ascending=False)
        .head(5)
        .round(2)
        .to_dict()
    )

    data = {"true": shap_true, "false": shap_false}

    assert isinstance(data, dict)
    return str(data)
