import functional_test_suite.tests.model_catalog.model_catalog as model_catalog
import functional_test_suite.apis.model_catalog_api as model_catalog_api
import functional_test_suite.constants.constants as constants
import functional_test_suite.helpers.requests_helper as requests_helper

def add_contract_helper(contract_type, model_slug):
    if model_slug == None:
        model_slug = model_catalog.add_model_version().json()["result"]["model_slug"]
    api = model_catalog_api.MODEL_CATALOG_API + "/version/" + model_slug + "-V1"
    if contract_type == "input":
        payload = constants.MODEL_CATALOG_DATA["add_input_contract"]
    else:
        payload = constants.MODEL_CATALOG_DATA["add_input_contract"]
    return requests_helper.patch_request(api, payload, True)