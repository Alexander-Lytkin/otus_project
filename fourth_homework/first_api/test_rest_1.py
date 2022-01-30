import pytest
import requests


class TestBreed:

    def test_get_sub_breeds(self):
        response = requests.get("https://dog.ceo/api/breed/hound/list")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["message"] == ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker']

    @pytest.mark.parametrize("breed", ["afghan", "basset", "blood", "english", "ibizan", "walker"])
    def test_get_list_images_from_sub_breed(self, breed):
        response = requests.get(f"https://dog.ceo/api/breed/hound/{breed}/images")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        breeds = []
        for i in data["message"]:
            var = i.split("/")[4]
            breeds.append(var)
        for var in breeds:
            assert f"hound-{breed}" == var

    @pytest.mark.parametrize("breed", ["afghan", "basset", "blood", "english", "ibizan", "walker"])
    @pytest.mark.parametrize("value", [1, 5, 9])
    def test_get_multiple_random_images_from_diff_sub_breed(self, breed, value):
        response = requests.get(f"https://dog.ceo/api/breed/hound/{breed}/images/random/{value}")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["message"] is not None
        assert len(data["message"]) == value

    def test_get_random_image_breed(self):
        response = requests.get("https://dog.ceo/api/breed/hound/images/random")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["message"] is not None

    @pytest.mark.parametrize("value", [-1, 0, 1, 5, 11])
    def test_get_multiple_random_image_breed(self, value):
        response = requests.get(f"https://dog.ceo/api/breed/hound/images/random/{value}")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["message"] is not None
        if value == -1:
            assert len(data["message"]) == 10
        elif value == 0:
            assert len(data["message"]) == 1
        else:
            assert len(data["message"]) == value

    @pytest.mark.xfail
    def test_get_multiple_random_image_breed_with_wrong_values(self):
        response = requests.get(f"https://dog.ceo/api/breed/hound/images/random/INVALID_VALUE")
        assert response.status_code == 400
        data = response.json()
        assert data["status"] == "bad request"
