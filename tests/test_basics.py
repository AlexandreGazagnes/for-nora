import pytest


@pytest.fixture
def random_id():

    return "848"


def test_fixture(random_id):

    assert random_id == "848"


@pytest.mark.parametrize(
    "result,operation",
    [
        (12, "6+6"),
        ((10, "4+6")),
    ],
)
def test_parametrize(result, operation):

    opp = eval(operation)
    assert result == opp
