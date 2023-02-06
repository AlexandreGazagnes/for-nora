import pickle


MODEL_FILE = "./assets/models/model.pk"
SHAP_FILE = "./assets/explainers/shap.pk"


def get_model():
    with open(MODEL_FILE, "rb") as f:
        pk = f.read()
        model = pickle.loads(pk)

    return model


def get_shap():
    with open(SHAP_FILE, "rb") as f:
        pk = f.read()
        explainer = pickle.loads(pk)

    return explainer
