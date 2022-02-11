import requests


def test_function(base_url, base_status_code):
    response = requests.get(base_url)
    assert response.status_code == int(base_status_code)
