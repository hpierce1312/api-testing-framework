import requests
import json
import functional_test_suite.tests.login.login as login
import functional_test_suite.constants.constants as constants

def set_verify(url):
    verify=True
    if 'https' in url:
        verify=False
    return verify

def get_access_token():
    access_token = login.login().json()["access_token"]
    return access_token

def get_headers(auth):
    if auth == True:
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + get_access_token()}
    else:
        headers = {"Content-Type": "application/json"}
    return headers

def get_request(api, auth):
    url = constants.DEFAULT_URL + api
    response = requests.get(url, headers=get_headers(auth), verify=set_verify(url))
    return response

def post_request(api, payload, auth):
    url = constants.DEFAULT_URL + api
    response = requests.post(url, data=json.dumps(payload), headers=get_headers(auth), verify=set_verify(url))
    return response

def patch_request(api, payload, auth):
    url = constants.DEFAULT_URL + api
    response = requests.patch(url, data=json.dumps(payload), headers=get_headers(auth), verify=set_verify(url))
    return response
