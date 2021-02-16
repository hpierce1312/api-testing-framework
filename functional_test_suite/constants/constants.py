import json

# JSON test data files
AUTH_DATA = json.load(open("functional_test_suite/data/auth.json"))
MODEL_CATALOG_DATA = json.load(open("functional_test_suite/data/model_catalog.json"))
WORKSPACES_DATA = json.load(open("functional_test_suite/data/workspaces.json"))
ORGANIZATION_ID = "4df4d256-394d-4488-a078-6bb05b4f3fe0"

DEFAULT_URL = AUTH_DATA["login"]["default_url"]