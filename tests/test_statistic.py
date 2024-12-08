def test_statistic(client):
    response = client.get("/statistic", params={"date": "2024-12-01"})
    assert response.status_code == 200
