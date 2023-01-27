import requests
import pytest

port = 8080
base = "http://127.0.0.1"


@pytest.fixture
def random_id():

    return "848"


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

    li = eval(r.text)
    assert isinstance(li, list)

    return li[:10]


def test_get_passenger():

    random_id = "848"

    url = f"{base}:{port}/get_passenger/{random_id}"
    r = requests.get(url)
    assert int(r.status_code) == 200

    print(r.text)


def test_predict():
    """test predict"""

    random_id = "848"

    url = f"{base}:{port}/predict/{random_id}"
    r = requests.get(url)
    assert int(r.status_code) == 200

    print(r.text)