import json
import functional_test_suite.tests.model_catalog.model_catalog as model_catalog

def test_list_models():
    assert model_catalog.list_models().status_code == 200

def test_add_model():
    assert model_catalog.add_model().status_code == 201
    assert model_catalog.add_model().json()["status"]["msg"] == "CatalogModelsCreateSuccess"

def test_add_model_version():
    assert model_catalog.add_model_version().status_code == 201
    assert model_catalog.add_model_version().json()["status"]["msg"] == "ModelVersionsUploadSuccess"

def test_add_input_contract():
    assert model_catalog.add_input_contract().status_code == 200

def test_add_output_contract():
    assert model_catalog.add_output_contract().status_code == 200