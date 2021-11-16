import json
import logging
import os

import allure
import requests

from dotenv import load_dotenv

load_dotenv()
class ApiMethods():

    proxy = {"http": "192.168.0.103:8080", "https": "192.168.0.103:8080"}

    def __init__(self):
        if "URL_ENV" in os.environ:
            self._api_url = os.environ["URL_ENV"]
        else:
            self._api_url = str(os.getenv("URL_ENV"))

    def logger_for_api(self, response):
        allure.attach("Request: \n url= {} \n header= {} \n body= {}".format(response.request.url, response.request.headers, json.dumps(response.request.body, indent=4)),
                      'request.txt', allure.attachment_type.TEXT)
        logging.info("Request: \n url= {} \n header= {} \n body= {}".format(response.request.url, response.request.headers, json.dumps(response.request.body, indent=4)))
        logging.info("Response: \n status={} \n header={} \n body={}".format(response.status_code, response.headers, json.dumps(response.json(), indent = 4)))

    def creds_logging(self, user_creds):
        username = user_creds
        logging.info(f"Credentials for API request:\nusername:{username}")
        return self

    def _get_method(self, url, headers=None, cookies="No", params=None, proxy=proxy):
        logging.info("Method: GET")
        url_request = self._api_url+url
        if cookies != "No":
            headers['Cookie'] = "language=en-gb; currency=USD; OCSESSID={}".format(cookies)
        response = requests.request("GET", url_request, headers=headers, params=params, proxies=proxy, verify=False)
        self.logger_for_api(response)
        return response

    def _post_method(self, url, body, cookies="No", params=None, headers=None, proxy=None):
        logging.info("Method: POST")
        url_request = str(self._api_url + url)
        if cookies != "No":
            headers['Cookie'] = "language=en-gb; currency=USD; OCSESSID={}".format(cookies)
        response = requests.request("POST", url_request, headers=headers, data=body, params=params, proxies=proxy)
        self.logger_for_api(response)
        return response

    def _put_method(self, url, body, headers=None, params=None, cookies="No", proxy=None):
        logging.info("Method: PUT")
        url_request = str(self._api_url + url)
        if cookies != "No":
            headers['Cookie'] = "language=en-gb; currency=USD; OCSESSID={}".format(cookies)
        response = requests.request("POST", url_request, headers=headers, data=body, params=params, proxies=proxy)
        self.logger_for_api(response)
        return response

    def _delete_method(self, url, headers=None, params=None, cookies="No", proxy=None):
        logging.info("Method: DELETE")
        url_request = str(self._api_url + url)
        if cookies != "No":
            headers['Cookie'] = "language=en-gb; currency=USD; OCSESSID={}".format(cookies)
        response = requests.request("POST", url_request, headers=headers, params=params, proxies=proxy)
        self.logger_for_api(response)
        return response