import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_info_endpoint(client):
    response = client.get('/api/info')
    assert response.status_code == 200
