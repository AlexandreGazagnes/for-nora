import pickle


def get_model(MODEL_FILE):
    with open(MODEL_FILE, "rb") as f:
        pk = f.read()
        model = pickle.loads(pk)

    return model


def get_shap(SHAP_FILE):
    with open(SHAP_FILE, "rb") as f:
        pk = f.read()
        explainer = pickle.loads(pk)

    return explainer
