def test_get_home(web_client):
    response = web_client.get("/")
    html = response.data.decode("utf-8")
    assert response.status_code == 200
    assert "Amputee Football World Cup 2018 – Mexico" in html

