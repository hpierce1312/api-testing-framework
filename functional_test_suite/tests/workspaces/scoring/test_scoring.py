import functional_test_suite.tests.workspaces.scoring.scoring as scoring

def test_add_scoring_workspace():
    assert scoring.add_scoring_workspace().status_code == 201