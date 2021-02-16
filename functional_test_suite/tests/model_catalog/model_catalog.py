import json
import functional_test_suite.helpers.requests_helper as requests_helper
import functional_test_suite.helpers.model_catalog_helper as model_catalog_helper
import functional_test_suite.apis.model_catalog_api as model_catalog_api
import functional_test_suite.constants.constants as constants

def list_models():
    return requests_helper.get_request(model_catalog_api.MODEL_CATALOG_API, True)

def add_model():
    payload = constants.MODEL_CATALOG_DATA["add_model"]
    return requests_helper.post_request(model_catalog_api.MODEL_CATALOG_API, payload, True)

def add_model_version():
    add_model()
    model_slug = add_model().json()["result"]["model_slug"]
    api = model_catalog_api.MODEL_CATALOG_API + "/" + model_slug + "/versions"
    payload = constants.MODEL_CATALOG_DATA["add_model_version"]
    return requests_helper.post_request(api, payload, True)

def add_input_contract(model_slug=None):
    return model_catalog_helper.add_contract_helper("input", model_slug)

def add_output_contract(model_slug=None):
    return model_catalog_helper.add_contract_helper("input", model_slug)

def add_both_contracts():
    model_slug = add_model_version().json()["result"]["model_slug"]
    add_input_contract(model_slug)
    add_output_contract(model_slug)
    return model_slug