import json
import functional_test_suite.constants.constants as constants
import functional_test_suite.apis.workspaces_api as workspaces_api
import functional_test_suite.helpers.requests_helper as requests_helper

def add_workspace(workspace_type):
    api = workspaces_api.WORKSPACES_API + "/" + constants.ORGANIZATION_ID
    if workspace_type == "serving":
        payload = constants.WORKSPACES_DATA[workspace_type]["add_serving_workspace"]
    elif workspace_type == "scoring_lite":
        payload = constants.WORKSPACES_DATA[workspace_type]["add_scoring_lite_workspace"]["workspaces"]
    else:
        payload = constants.WORKSPACES_DATA[workspace_type]["add_scoring_workspace"]["workspaces"]
    return requests_helper.post_request(api, payload, True)

def add_scoring_workspace(workspace_type):
    workspace_id = json.loads(add_workspace(workspace_type).json()["result"])["workspace_id"]
    api = workspaces_api.WORKFLOW_MANAGERS_API + "/" + workspace_id
    payload = constants.WORKSPACES_DATA[workspace_type]["add_" + workspace_type + "_workspace"]["workflow_managers"]
    return requests_helper.post_request(api, payload, True)