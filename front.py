import os, sys, logging, warnings
from random import shuffle

import streamlit as st

import pandas as pd
import numpy as np

import requests

port = 8080
base = "http://127.0.0.1"
option = "None"


def _extract_request(url):

    # get
    r = requests.get(url)
    assert int(r.status_code) == 200

    print(r.text)

    # eval
    dd = eval(r.text)
    assert isinstance(dd, dict)

    print(dd)

    return dd


# @st.cache
def get_ids(n=30):
    """get ids"""

    url = f"{base}:{port}/getids"
    print("\n\n" + url)

    return _extract_request(url)


# @st.cache
def get_model_decision():

    url = f"{base}:{port}/model_decision"
    print("\n\n" + url)

    return _extract_request(url)


def get_passenger(_id):

    url = f"{base}:{port}/get_passenger/{_id}"
    print("\n\n" + url)

    return _extract_request(url)


def get_predict(_id):
    """test predict"""

    url = f"{base}:{port}/predict/{_id}"
    print("\n\n" + url)

    return _extract_request(url)


def get_explainer(_id):

    url = f"{base}:{port}/explain/{_id}"
    print("\n\n" + url)

    return _extract_request(url)


#######################
#######################


# cache
id_list = get_ids()["id_list"]
print(id_list)
np.random.shuffle(id_list)
print(id_list)
model_dec = get_model_decision()


# title

st.title("APP PREDICTION")

# ID
_id = st.selectbox("id", id_list)
st.write("You selected:", _id)


# data
passenger = get_passenger(_id)
# predict = get_predict(str(_id))
# explainer = get_explainer(str(_id))


# info
st.write("passenger:", "\t", str(passenger))
# st.write("predict:", "\t", str(predict))
# st.write("explainer:", "\t", str(explainer))
# st.write("model_dec" "\t", str(model_dec))
