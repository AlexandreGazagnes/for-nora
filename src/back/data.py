"""

"""

import os

import pandas as pd


def get_df(filename: str) -> pd.DataFrame:
    """ """

    return pd.read_csv(filename)


def get_passenger_id(filename: str) -> list:
    """ """

    passengers_id_list = list(get_df(filename).PassengerId.values)

    return passengers_id_list


def extract_vect(
    _id: int,
    df: pd.DataFrame,
    id_col: str = "PassengerId",
    target_col: str = "Survived",
) -> tuple:
    """extract from a df"""

    _id = int(_id)

    X = df.copy().loc[df[id_col] == _id]
    assert len(X) == 1

    id_val = X[id_col].iloc[0]
    target_val = X[target_col].iloc[0]

    drop_cols = [id_col, target_col]
    X = X.drop(columns=drop_cols)
    ser = X.iloc[0].to_dict()

    return ser, id_val, target_val
