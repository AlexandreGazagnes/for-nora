
import pickle 

def get_model() : 

    with open("./models/model.pk", "rb") as f:
        pk = f.read()
        model = pickle.loads(pk)

    return model


def get_shap() : 

    with open("./explainers/shap.pk", "rb") as f:
        pk = f.read()
        explainer = pickle.loads(pk)

    return explainer