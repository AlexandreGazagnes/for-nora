import streamlit as st
import pandas as pd

import requests

port = 8080
base = "http://127.0.0.1"


def get_ids():
    """get ids """

    url = base + ":" + str(port) + "/getids"
    r = requests.get(url + "")
    assert int(r.status_code) == 200

    li = eval(r.text)
    assert isinstance(li, list)

    return li


option = st.selectbox("How would you like to be contacted?", get_ids())

st.write("You selected:", option)
