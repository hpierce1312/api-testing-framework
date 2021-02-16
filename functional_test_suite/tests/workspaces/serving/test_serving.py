import functional_test_suite.tests.workspaces.serving.serving as serving

def test_add_serving_workspace():
    assert serving.add_serving_workspace().status_code == 201

def test_add_publisher():
    assert serving.add_publisher().status_code == 201

def test_add_challenger():
    assert serving.add_challenger().status_code == 201