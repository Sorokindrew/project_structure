import pytest
from pytest import fixture
from fastapi.testclient import TestClient
from sample_project.main import app


@pytest.fixture(autouse=True)
def client():
    client = TestClient(app)
    yield client
