import functional_test_suite.tests.workspaces.common.workspaces as workspaces

def test_list_workspaces():
    assert workspaces.list_workspaces().status_code == 200