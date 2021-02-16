import functional_test_suite.tests.workspaces.scoring_lite.scoring_lite as scoring_lite

def test_add_scoring_lite_workspace():
    assert scoring_lite.add_scoring_lite_workspace().status_code == 201