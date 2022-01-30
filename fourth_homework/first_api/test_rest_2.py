import pytest
import requests
from jsonschema import validate


class TestGetBrewery:

    def test_get_list_brewery(self):
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "street": {"type": "string"},
                "city": {"type": "string"},
                "state": {"type": "string"},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": "string"},
                "latitude": {"type": "string"},
                "phone": {"type": "string"},
                "updated_at": {"type": "string"},
                "created_at": {"type": "string"},
            },
            "required": ["id", "name", "state", "country", "created_at", "postal_code"]
        }
        response = requests.get("https://api.openbrewerydb.org/breweries")
        assert response.status_code == 200
        data = response.json()[0]
        validate(instance=data, schema=schema)
        assert len(data) > 0

    def test_get_brewery_by_city(self):
        response = requests.get("https://api.openbrewerydb.org/breweries?by_city=san_diego")
        assert response.status_code == 200
        data = response.json()[0]
        assert data["city"] == "San Diego"
        assert data["state"] == "California"

    @pytest.mark.parametrize("state", ["Ohio", "New York"])
    def test_get_brewery_by_state(self, state):
        response = requests.get(f"https://api.openbrewerydb.org/breweries?by_state={state}")
        assert response.status_code == 200
        data = response.json()[0]
        assert data["state"] == state

    @pytest.mark.parametrize("state", [-1, 0])
    def test_get_brewery_by_wrong_value(self, state):
        response = requests.get(f"https://api.openbrewerydb.org/breweries?by_state={state}")
        assert response.status_code == 200
        data = response.json()
        assert data == []

    @pytest.mark.parametrize("number", [0, 4, 10])
    def test_get_brewery_by_number(self, number):
        response = requests.get(f"https://api.openbrewerydb.org/breweries?per_page={number}")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == number
