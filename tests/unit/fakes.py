import pytest

from orchestration.server import app


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    client = app.app.test_client()

    yield client
