
def test_get_service(client):
    response = client.get('/v1/orchestration/services/testing')
    assert response.status_code == 200
    assert "Hello World!" == response.data
