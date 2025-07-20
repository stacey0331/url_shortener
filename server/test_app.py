import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_shorten_url(client):
    res = client.post('/api/shorten', json={"original_url": "https://www.google.com"})
    assert res.status_code == 200
    data = res.get_json()
    assert 'short_url' in data

def test_shorten_url_without_scheme(client):
    res = client.post('/api/shorten', json={"original_url": "www.google.com"})
    assert res.status_code == 200
    data = res.get_json()
    assert 'short_url' in data

def test_shorten_url_same_short_url(client):
    res1 = client.post('/api/shorten', json={"original_url": "https://www.google.com"})
    res2 = client.post('/api/shorten', json={"original_url": "www.google.com"})
    assert res1.status_code == 200
    assert res2.status_code == 200
    data1 = res1.get_json()
    data2 = res2.get_json()
    assert data1.get('short_url') == data2.get('short_url')
