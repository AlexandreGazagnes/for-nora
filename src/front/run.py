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


# data
passenger = get_passenger(BASE_URL, _id)
# predict = get_predict(str(_id))
# explainer = get_explainer(str(_id))


# info
st.write("passenger:", "\t", str(passenger))
# st.write("predict:", "\t", str(predict))
# st.write("explainer:", "\t", str(explainer))
# st.write("model_dec" "\t", str(model_dec))
