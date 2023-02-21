import pytest

import pandas as pd
import numpy as np

import requests

from back import create_app


port = 8080
base = "http://127.0.0.1"


@pytest.fixture
def ids_list():
    df = pd.read_csv("./data/cleaned/df_train.csv")
    passengers_id_list = list(df.PassengerId.values)

    return passengers_id_list


@pytest.fixture
def app():
    app = create_app()

    return app


def test_hello():
    """test hello"""

    url = f"{base}:{port}/"
    r = requests.get(url + "")

    assert int(r.status_code) == 200


def test_get_ids():
    """test get ids"""

    url = f"{base}:{port}/getids"
    r = requests.get(url)
    assert int(r.status_code) == 200

    data = eval(r.text)
    assert isinstance(data, dict)

    print(str(li[:10]))

    data = str({"id_list": li[:30]})

    return data


@pytest.mark.parametrize("random_id", ids_list)
def test_get_passenger(random_id):
    url = f"{base}:{port}/get_passenger/{random_id}"
    r = requests.get(url)
    assert int(r.status_code) == 200

    print(r.text)

    return r.text


def test_predict(random_id):
    url = f"{base}:{port}/predict/{random_id}"
    r = requests.get(url)
    assert int(r.status_code) == 200

    print(r.text)

    return r.text


def test_model_decision():
    url = f"{base}:{port}/model_decision"
    r = requests.get(url)
    assert int(r.status_code) == 200

    print(r.text)

    return r.text


def test_explaier(random_id):
    url = f"{base}:{port}/explain/{random_id}"
    r = requests.get(url)
    assert int(r.status_code) == 200

    print(r.text)

    return r.text
