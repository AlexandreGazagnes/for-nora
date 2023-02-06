import pytest

import pandas as pd
from random import choice, choices

from src.back.data import *


def test_df():
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 10
    assert df.shape[1] > 5

    assert "Survived" in df.columns
    assert "PassengerId" in df.columns


def test_PassegenID():
    ser = pd.Series(passengers_id_list)

    assert len(ser) == ser.nunique()


def test_extract_vect():
    for _ in range(10):
        _id = choice(passengers_id_list)
        ser, Passenger_id, Survived = extract_vect(str(_id), df)


@pytest.mark.parametrize("_id", passengers_id_list[-10:])
def test_extract_vect_2(_id):
    ser, Passenger_id, Survived = extract_vect(str(_id), df)
