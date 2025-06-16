
import requests
import allure


@allure.title("Test GET request to Novele website")
def test_novele_website_status():
    url = "https://www.novele.com/"
    response = requests.get(url)

    with allure.step(f"GET {url}"):  # to record GET，allure to generate formatted report
        assert response.status_code == 200


@allure.title("Test POST request with sample data")
def test_post_request():
    url = "https://httpbin.org/post"  #  POST API
    data = {
        "username": "testuser",
        "password": "123456"
    }

    with allure.step("Send POST request"):
        response = requests.post(url, data=data)
        assert response.status_code == 200

    with allure.step("Check response content"):
        json_data = response.json()
        assert json_data["form"]["username"] == "testuser"
        assert json_data["form"]["password"] == "123456"