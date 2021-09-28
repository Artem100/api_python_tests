import allure

from src.api_response_actions import ResponseActions
from src.api_services import UsersApi
from src.json import Json


class TestApi:

    @allure.title("Get second page of users and present email in json body at first collection")
    def test_01(self):
        response = UsersApi().getUsersPagesList("2")
        ResponseActions().status_code_check(response, 200)
        ResponseActions().check_value_by_path(response, "$.data[0].email", "michael.lawson@reqres.in")
        # Take list of all keys first_name
        first_name_list = [d['first_name'] for d in response.json()['data']]
        # print(first_name_list)

    @allure.title("Check last_name value in response body")
    def test_02(self):
        last_name = "Ferguson"
        response = UsersApi().getUsersPagesList("2")
        ResponseActions().status_code_check(response, 200)
        # If we want to use generator
        first_name_list = [d['last_name'] for d in response.json()['data']]
        # Look how to do with jsonpath-rw
        ResponseActions().value_in_body_from_list_by_path(response, "$.data[*].last_name", last_name)

    @allure.title("Create user")
    def test_03(self, faker_fixture):
        name = faker_fixture.word()
        job = faker_fixture.name()
        response = UsersApi().create_new_user(Json.create_user(name, job))
        ResponseActions().status_code_check(response, 201)
        ResponseActions().check_value_by_path(response, "$.name", name)
        ResponseActions().check_value_by_path(response, "$.job", job)
        ResponseActions().check_value_more_null(response, "$.id")
