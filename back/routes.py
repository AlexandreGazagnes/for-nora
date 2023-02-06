from back.data import * 
from back.pks import * 

from flask import jsonify

import shap




def _hello() : 

    data = {"msg": "<p>Hello, World!</p>"}

    return jsonify(data)


def _getids(): 

    li = passengers_id_list[:30]
    logging.warning(li)

    data = {"id_list": li[:30]}

    return jsonify(data)


def _get_passenger(_id) : 

    data, _id, _target = extract_vect(_id, df)

    return jsonify(data)


def _get_prediction(_id) : 

    # extract
    dd, _id, _target = extract_vect(_id, df)
    # ans = model.predict(pd.Series(dd))

    # build object predictable
    logging.warning(dd)
    ser = pd.Series(dd)
    logging.warning(ser)
    local_df = pd.DataFrame([ser])

    # pred and proba
    pred = model.predict(local_df)[0]
    proba = model.predict_proba(local_df)[0]

    # ans
    data = {"pred": pred, "proba": proba.tolist()}

    return jsonify(data)



def _get_model_decision() : 

    data = {
        k: v.round(2)
        for v, k in zip(model.feature_importances_, model.feature_names_in_)
    }
    return jsonify(data)


def _get_explaination(_id) : 

        dd, _id, _target = extract_vect(_id, df)

        shap_values = explainer.shap_values(pd.DataFrame([dd]))
        shap_false = shap_values[0]
        shap_true = shap_values[1]

        cols = pd.DataFrame([dd]).columns

        # true / false
        shap_true = (
            pd.DataFrame(shap_true, columns=cols)
            .iloc[0]
            .sort_values(ascending=False)
            .head(5)
            .round(2)
            .to_dict()
        )
        shap_false = (
            pd.DataFrame(shap_false, columns=cols)
            .iloc[0]
            .sort_values(ascending=False)
            .head(5)
            .round(2)
            .to_dict()
        )

        data = {"true": shap_true, "false": shap_false}

        return jsonify(data)