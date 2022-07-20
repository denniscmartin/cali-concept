import pytest
from web import create_app


@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()

    return client
