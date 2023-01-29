import requests
from config import SINGLE_USER_URL

def test_single_user():
    # Make a GET request to the endpoint
    response = requests.get(SINGLE_USER_URL)

    # Assert that the status code is 200
    assert response.status_code == 200

    # Assert that the first_name field in the response is "Janet" (optional)
    assert response.json()["first_name"] == "Janet"
