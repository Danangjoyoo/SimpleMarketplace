
def test_post_product(client):
    data = {
        "name": "Test Product Name",
        "description": "Test Product Description"
    }
    response = client.post("/product/add", json=data)
    assert response.status_code == 200

def test_post_product(client):
    data = {
        "name": "Test Product Name",
        "description": "Test Product Description"
    }
    client.post("/product/add", json=data)
    response = client.get("/product")
    assert response.status_code == 200
    assert response.json == [data]