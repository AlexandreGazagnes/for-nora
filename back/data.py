import pandas as pd


df = pd.read_csv("./data/cleaned/df_train.csv")


passengers_id_list = list(df.PassengerId.values)


def extract_vect(PassengerId, _df):
    """extract from a df"""

    PassengerId = int(PassengerId)

    X = _df.loc[_df.PassengerId == PassengerId].copy()
    assert len(X) == 1

    Passenger_id = X.PassengerId[0]
    Survived = X.Survived[0]
    X = X.drop(columns=["PassengerId", "Survived"])
    ser = X.iloc[0].to_dict()

    return ser, Passenger_id, Survived


