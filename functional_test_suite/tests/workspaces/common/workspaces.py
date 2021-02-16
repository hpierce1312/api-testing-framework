import functional_test_suite.helpers.requests_helper as requests_helper
import functional_test_suite.apis.workspaces_api as workspaces_api
import functional_test_suite.constants.constants as constants

def list_workspaces():
    api = workspaces_api.WORKSPACES_API + "/" + constants.ORGANIZATION_ID
    return requests_helper.get_request(api, True)