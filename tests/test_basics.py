import os, subprocess

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



def test_python_v() : 

    # The shell command to run
    command = "python --version"

    # Run the shell command
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the standard output and error as bytes
    output = result.stdout
    error = result.stderr

    # Decode the bytes to strings (if necessary)
    output_str = output.decode("utf-8")
    error_str = error.decode("utf-8")

    # Print the output and error
    print("Output:")
    print(output_str)
    print("Error:")
    print(error_str)

    output_list = output_str.split(".")

    assert output_list[1] == "8"

def test_python_env() : 

    # The shell command to run
    command = "which python"

    # Run the shell command
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the standard output and error as bytes
    output = result.stdout
    error = result.stderr

    # Decode the bytes to strings (if necessary)
    output_str = output.decode("utf-8")
    error_str = error.decode("utf-8")

    # Print the output and error
    print("Output:")
    print(output_str)
    print("Error:")
    print(error_str)

