import os, sys, logging, warnings
from random import shuffle

import streamlit as st

import pandas as pd
import numpy as np

import requests


from src.front.cache import *
from src.front.get import *


# title

st.title("APP PREDICTION")

# ID
_id = st.selectbox("id", id_list)
st.write("You selected:", _id)


# passenger
passenger = get_passenger(BASE_URL, _id)
passenger = pd.DataFrame([passenger]).T
st.table(passenger)


predict = get_prediction(BASE_URL, str(_id))
explainer = get_shap(BASE_URL, str(_id))


# info
st.write("predict:", "\t", str(predict))
st.write("explainer:", "\t", str(explainer))

# model decision
st.write("model_dec" "\t", str(model_dec))
model_dec = pd.DataFrame([model_dec]).T
st.bar_chart(model_dec)


explainer = get_shap(BASE_URL, str(_id))
true = [("true", k, v) for k, v in explainer["true"].items()]
false = [("false", k, -v) for k, v in explainer["false"].items()]
true_fasle = true + false

vals = pd.DataFrame(true + false, columns=["_decision", "_feature", "_value"])


st.table(vals)

pivot = vals.pivot(index="_feature", columns="_decision", values="_value")


st.table(pivot)
st.bar_chart(pivot)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.table(chart_data)

st.bar_chart(chart_data)
