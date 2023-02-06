import os, sys, logging

from flask import Flask

from src.back.app import create_app


# import pickle, os, sys, logging

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

# shap.initjs()


BACK_DEBUG = True
BACK_PORT  = 8080
BACK_HOST  = "0.0.0.0"



if __name__ == "__main__":

    app = create_app()
    app.run(debug=BACK_DEBUG, port=BACK_PORT, host=BACK_HOST,)
