import json
import functional_test_suite.helpers.requests_helper as helper
import functional_test_suite.apis.login_api as login_api
import functional_test_suite.constants.constants as constants

def login():
    payload = {
        "email": constants.AUTH_DATA["login"]["email"], 
        "password": constants.AUTH_DATA["login"]["password"]
        }
    return helper.post_request(login_api.LOGIN, payload, False)

