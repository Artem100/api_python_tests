import json
import logging
import os
from jsonschema import validate

import jsonpath_rw

from conftest import ROOT_DIR


class ResponseActions(object):
    # https://jsonpath.com
    # https://goessner.net/articles/JsonPath/
    # https://jsonpath-rw.readthedocs.io/


    # Пример без использования плагина *jsonpath-rw*
    def history_response_json(self, response, vessel, location, rotation_date):
        data = json.loads(response.text)
        data_json = json.dumps(data, indent=2)
        logging.info("Check response body *Rotation ETA*")

        try:
            vessel_key = data['data']['dataHistory'][0]['vessel']
            location_key = data['data']['dataHistory'][0]['rotations'][0]['location']
            date_key = data['data']['dataHistory'][0]['rotations'][0]['date']
        except Exception as e:
            logging.error(f"Response body doesn't has field: {e}\nResponse body: {data_json}")
            assert False, f"Response body doesn't has field: {e}"

        try:
            assert vessel_key == vessel, f"*Vessel* key fail: \nActual value {vessel_key}\nExpected value: {vessel}"
            assert location_key == location, f"*Location* key fail: \nActual value {location_key}\nExpected value: {location}"
            assert date_key == rotation_date, f"*Date* key fail: \nActual value {date_key}\nExpected value: {rotation_date}"
        except Exception as e:
            logging.error(f"Fail by reason: {e}\nResponse body: {data_json}")
            assert False, f"Fail by reason: {e}"

    def status_code_check(self, response, expected_code=200):
        logging.info(f"Check status is code: {expected_code}")
        if response.status_code == expected_code:
            pass
        else:
            logging.info(f"Incorrect status code. \nExpected value: 200,\n  Actual value: {response.status_code}")
            raise AssertionError(f"Incorrect status code. \nExpected value: 200,\n  Actual value: {response.status_code}")


    def check_value_by_path(self, response, json_path, check_value):
        logging.info(f"Check value in key: {json_path}")
        try:
            logging.info("Key by path: *{}* has value: {}".format(json_path, check_value))
            json = response.json()
            value = jsonpath_rw.parse(json_path).find(json)[0].value
            assert value == check_value
        except KeyError:
            logging.info("\nResponse body doesn't have *{}* field".format(json_path))
            assert Exception, "\nResponse body doesn't have *{}* field".format(json_path)
        except AssertionError:
            logging.info(f"\nKey [{json_path}] hasn't value: '{check_value}' \nIt's has value: '{value}'")
            assert False, f"\nKey [{json_path}] hasn't value: '{check_value}' \nIt's has value: '{value}'"

    def check_value_more_null(self, response, json_path):
        logging.info(f"Check value in key: {json_path}")
        try:
            logging.info("Key {} has value than 0".format(json_path))
            json = response.json()
            value = jsonpath_rw.parse(json_path).find(json)[0].value
            assert len(value) > 0
        except KeyError:
            logging.info("\nResponse body doesn't have *{}* field".format(json_path))
            assert Exception, "\nResponse body doesn't have *{}* field".format(json_path)
        except AssertionError:
            logging.info(f"No")
            assert False, f"No"

    def json_body_check_full(self, response_body, check_json):
        try:
            logging.info(f"Check value in response body")
            json = response_body.json()
            assert json == check_json
        except AssertionError:
            logging.info(f"Jsons aren't qual\nResponse json:\n{json}\nChecking json:\n{check_json}")
            assert False, f"No"

    def value_in_body_from_list_by_path(self, response, json_path, check_value):
        logging.info(f"Check value in key: {json_path}")
        try:
            logging.info("Make list from values by path: {}".format(json_path))
            json = response.json()
            # value_list = jsonpath_rw.parse(json_path).find(json)[0].value
            value_list = jsonpath_rw.parse(json_path).find(json)[0]
            tt = type(value_list)
            print(tt)
            assert check_value in value_list
        except KeyError:
            logging.info("\nResponse body doesn't have *{}* field".format(json_path))
            assert Exception, "\nResponse body doesn't have *{}* field".format(json_path)
        except AssertionError:
            logging.info(f"\nKey [{json_path}] hasn't value: '{check_value}' \nIt's has value: '{value_list}'")
            assert False, f"\nKey [{json_path}] hasn't value: '{check_value}' \nIt's has value: '{value_list}'"

    @staticmethod
    def validate_json_body(response_json, file_name_schema):
        path_file = os.path.join((ROOT_DIR + file_name_schema))
        with open(path_file) as f:
            validate(instance=response_json.json(), schema=json.loads(f.read()))

