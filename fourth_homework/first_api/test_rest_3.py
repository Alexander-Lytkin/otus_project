import pytest
import requests
from jsonschema import validate


class TestJsonPlaceholder:

    def test_get_placeholder(self):
        schema = {
            "type": "object",
            "properties": {
                "userId": {"type": "integer"},
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "body": {"type": "string"},
            },
            "required": ["userId", "id", "title", "body"]
        }
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        assert response.status_code == 200
        data = response.json()[0]
        validate(instance=data, schema=schema)
        assert len(data) > 0

    def test_get_json_placeholder_users(self):
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "username": {"type": "string"},
                "email": {"type": "string"},
            },
            "required": ["id", "name", "username", "email"]
        }
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        assert response.status_code == 200
        data = response.json()
        user = response.json()[0]
        validate(instance=user, schema=schema)
        assert len(data) == 10

    @pytest.mark.parametrize("id", [1, 2, 3])
    def test_get_posts_by_id(self, id):
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == id

    @pytest.mark.parametrize("id", [-1, "INVALID_ID"])
    def test_get_posts_by_wrong_id(self, id):
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
        assert response.status_code == 404
        data = response.json()
        assert data == {}

    @pytest.mark.parametrize("id", [1, 5, 9])
    def test_get_comments_by_post_id(self, id):
        response = requests.get(f"https://jsonplaceholder.typicode.com/comments?postId={id}")
        assert response.status_code == 200
        data = response.json()
        for post_id in data:
            assert post_id["postId"] == id
