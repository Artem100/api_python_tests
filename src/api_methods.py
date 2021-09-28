import json
import logging
import os
import requests

from dotenv import load_dotenv

load_dotenv()
class ApiMethods():

    def __init__(self):
        if "URL_ENV" in os.environ:
            self._api_url = os.environ["URL_ENV"]
        else:
            self._api_url = str(os.getenv("URL_ENV"))

    def logger_for_api(self, response):
        logging.info("Request: \n url= {} \n header= {} \n body= {}".format(response.request.url, response.request.headers, json.dumps(response.request.body, indent=4)))
        logging.info("Response: \n status={} \n header={} \n body={}".format(response.status_code, response.headers, json.dumps(response.json(), indent = 4)))

    def creds_logging(self, user_creds):
        username = user_creds
        logging.info(f"Credentials for API request:\nusername:{username}")
        return self

    def _get_method(self, url, content_type='application/json', cookies="No", params=""):
        logging.info("Method: GET")
        url_request = self._api_url+url
        headers = {'content-type': content_type}
        if cookies != "No":
            headers['Cookie'] = "language=en-gb; currency=USD; OCSESSID={}".format(cookies)
        response = requests.request("GET", url_request, headers=headers, params=params)
        self.logger_for_api(response)
        return response

    def _post_method(self, url, body, cookies="No", params=""):
        logging.info("Method: POST")
        url_request = str(self._api_url + url)
        # headers = {'content-type': content_type}
        if cookies != "No":
            headers['Cookie'] = "language=en-gb; currency=USD; OCSESSID={}".format(cookies)
        else:
            response = requests.request("POST", url_request, data=body, params=params)
        self.logger_for_api(response)
        return response

    def _put_method(self, url, body, content_type='application/json', cookies="No"):
        logging.info("Method: PUT")
        url_request = str(self._api_url + url)
        headers = {'content-type': content_type}
        if cookies != "No":
            headers['Cookie'] = "language=en-gb; currency=USD; OCSESSID={}".format(cookies)
        response = requests.request("POST", url_request, headers=headers, data=body)
        self.logger_for_api(response)
        return response

    def _delete_method(self, url, content_type='application/json', cookies="No"):
        logging.info("Method: DELETE")
        url_request = str(self._api_url + url)
        headers = {'content-type': content_type}
        if cookies != "No":
            headers['Cookie'] = "language=en-gb; currency=USD; OCSESSID={}".format(cookies)
        response = requests.request("POST", url_request, headers=headers)
        self.logger_for_api(response)
        return response