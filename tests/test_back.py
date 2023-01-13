import requests
import pytest

port = 8080
base = "http://127.0.0.1"


def test_hello():
    """test hello"""

    url = base + ":" + str(port) + "/"
    r = requests.get(url + "")
    assert int(r.status_code) == 200


def test_get_ids():
    """test get ids"""

    url = base + ":" + str(port) + "/getids"
    r = requests.get(url + "")
    assert int(r.status_code) == 200

    li = eval(r.text)
    assert isinstance(li, list)


def test_predict():
    """test predict"""

    url = base + ":" + str(port) + "/predict/1234"
    r = requests.get(url + "")
    assert int(r.status_code) == 200

    ans = eval(r.text)
    assert ans in [0, 1, "0", 1]