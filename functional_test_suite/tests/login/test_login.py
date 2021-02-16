import functional_test_suite.tests.login.login as login

def test_login():
    assert login.login().status_code == 200

