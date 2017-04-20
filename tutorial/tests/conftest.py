import pytest
from falcon import testing
from tutorial import create_app

@pytest.fixture(scope = 'module')
def client():
  return testing.TestClient(create_app())
