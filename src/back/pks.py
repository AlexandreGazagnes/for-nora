"""

"""
import os, pickle, warnings, logging


def read_pk(filename: str) -> object:
    """ """

    logging.info(filename)

    with open(filename, "rb") as f:
        pk = f.read()
        model = pickle.loads(pk)

    return model
