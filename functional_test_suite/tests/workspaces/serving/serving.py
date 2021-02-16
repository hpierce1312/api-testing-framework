import json
import functional_test_suite.apis.serving_api as serving_api
import functional_test_suite.helpers.workspaces_helper as workspaces_helper
import functional_test_suite.helpers.requests_helper as requests_helper
import functional_test_suite.constants.constants as constants
import functional_test_suite.tests.model_catalog.model_catalog as model_catalog

def add_serving_workspace():
    return workspaces_helper.add_workspace("serving")

def add_publisher(workspace_id=None):
    workspace_id = json.loads(add_serving_workspace().json()["result"])["workspace_id"]
    api = serving_api.PUBLISHERS_API + "/" + workspace_id
    payload = constants.WORKSPACES_DATA["serving"]["add_publisher"]
    payload["model_slug"] = model_catalog.add_both_contracts()
    return requests_helper.post_request(api, payload, True)

def add_challenger(workspace_id=None):
    workspace_id = json.loads(add_serving_workspace().json()["result"])["workspace_id"]
    api = serving_api.CHALLENGERS_API + "/" + workspace_id
    payload = constants.WORKSPACES_DATA["serving"]["add_challenger"]
    return requests_helper.post_request(api, payload, True)

def add_publisher_and_challenger():
    workspace_id = json.loads(add_serving_workspace().json()["result"])["workspace_id"]
    add_publisher(workspace_id)
    add_challenger(workspace_id)
    