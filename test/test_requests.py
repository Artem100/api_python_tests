import json
import os

import allure

from conftest import ROOT_DIR
from src.api_response_actions import ResponseActions
from src.api_services import UsersApi
from src.json_bodies import Json
from jsonschema import validate


class TestApi:

    @allure.title("Get second page of users and present email in json body at first collection")
    def test_01(self):
        response = UsersApi().getUsersPagesList("2")
        ResponseActions().status_code_check(response, 200)
        ResponseActions().check_value_by_path(response, "$.data[0].email", "michael.lawson@reqres.in")
        # Take list of all keys first_name
        first_name_list = [d['first_name'] for d in response.json()['data']]
        # print(first_name_list)

    # @allure.title("Check last_name value in response body use jsonpath-rw")
    # def test_02_1(self):
    #     last_name = "Ferguson"
    #     response = UsersApi().getUsersPagesList(2)
    #     type(response)
    #     ResponseActions().status_code_check(response, 200)
    #     # Look how to do with jsonpath-rw
    #     ResponseActions().value_in_body_from_list_by_path(response, "$.data[*].last_name", last_name)

    @allure.title("Check last_name value in response body user use generator")
    def test_02_2(self):
        last_name = "Ferguson"
        response = UsersApi().getUsersPagesList(2)
        type(response)
        ResponseActions().status_code_check(response, 200)
        first_name_list = [d['last_name'] for d in response.json()['data']]
        print(first_name_list)

    @allure.title("Create new user")
    def test_03(self, faker_fixture):
        name = faker_fixture.word()
        job = faker_fixture.name()
        response = UsersApi().create_new_user(Json.create_user(name, job))
        ResponseActions().status_code_check(response, 201)
        ResponseActions().check_value_by_path(response, "$.name", name)
        ResponseActions().check_value_by_path(response, "$.job", job)
        ResponseActions().check_value_more_null(response, "$.id")

    @allure.title("Get info about user and check all fields")
    def test_04(self):
        user_id = 2
        check_body = Json.view_single_user_json(id=user_id, email="janet.weaver@reqres.in", first_name = "Janet",
                                               last_name="Weaver", avatar="https://reqres.in/img/faces/2-image.jpg",
                                               support_url="https://reqres.in/#support-heading",
                                               text="To keep ReqRes free, contributions towards server costs are appreciated!")

        response = UsersApi().view_single_user(str(user_id))
        ResponseActions().status_code_check(response)
        ResponseActions().json_body_check_full(response, check_body)


