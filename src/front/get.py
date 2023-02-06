import requests

def _extract_request(url):

    # get
    r = requests.get(url)
    assert int(r.status_code) == 200

    print(r.text)

    # eval
    dd = eval(r.text)
    assert isinstance(dd, dict)

    print(dd)

    return dd


# @st.cache
def get_ids(base, n=30):
    """get ids"""

    url = f"{base}/getids"
    print("\n\n" + url)

    return _extract_request(url)


# @st.cache
def get_model_decision(base):

    url = f"{base}/model_decision"
    print("\n\n" + url)

    return _extract_request(url)


def get_passenger(base, _id):

    url = f"{base}/get_passenger/{_id}"
    print("\n\n" + url)

    return _extract_request(url)


def get_predict(base, _id):
    """test predict"""

    url = f"{base}/predict/{_id}"
    print("\n\n" + url)

    return _extract_request(url)


def get_explainer(base, _id):

    url = f"{base}/explain/{_id}"
    print("\n\n" + url)

    return _extract_request(url)


#######################
#######################


