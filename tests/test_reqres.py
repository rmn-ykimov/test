"""
Module for testing a single user endpoint.

This module contains a single function, `test_single_user`, which makes a GET
request to the endpoint specified in the SINGLE_USER_URL constant from the
config module. The response from the endpoint is then checked for a 200 status
code and, if found, the "first_name" key in the JSON response is checked for
the value "Janet".
"""
import requests
from config import SINGLE_USER_URL

def test_single_user():
    """
    Test a single user endpoint.

    This function makes a GET request to the endpoint specified in the
    SINGLE_USER_URL constant from the config module. The response from the
    endpoint is then checked for a 200 status code and, if found, the
    "first_name" key in the JSON response is checked for the value "Janet".
    """
    # Make a GET request to the endpoint
    response = requests.get(SINGLE_USER_URL)

    # Assert that the status code is 200
    assert response.status_code == 200

    # Assert that the first_name field in the response is "Janet"
    assert response.json()["first_name"] == "Janet"
