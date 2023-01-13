import streamlit as st
import pandas as pd

import requests

port = 8080
base = "http://127.0.0.1"


option = "None"


def get_ids():
    """get ids """

    url = base + ":" + str(port) + "/getids"
    r = requests.get(url + "")
    assert int(r.status_code) == 200

    li = eval(r.text)
    assert isinstance(li, list)

    return li


def predict(id):
    """predict and id"""

    url = base + ":" + str(port) + "/predict/" + str(id)
    r = requests.get(url + "")
    assert int(r.status_code) == 200

    ans = eval(r.text)
    assert ans in [0, 1, "0", 1]

    return ans


# selection
option = st.selectbox("How would you like to be contacted?", get_ids())
st.write("You selected:", option)


# pred
if isinstance(option, int):
    ans = predict(option)
    ans = "CREDIT ACCORDé" if ans else "CREDIT REFUSé"
    st.write(f"la réponse est {ans}")