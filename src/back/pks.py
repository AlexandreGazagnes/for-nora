import os, pickle, warnings, logging


MODEL_FILE = os.getenv("MODEL_FILE")
SHAP_FILE = os.getenv("SHAP_FILE")


def read_pk(fn):
    """ """

    logging.info(fn)

    with open(fn, "rb") as f:
        pk = f.read()
        model = pickle.loads(pk)

    return model
