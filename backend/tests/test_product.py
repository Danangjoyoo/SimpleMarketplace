
def test_post_product(client):
    data = {
        "name": "Test Product Name",
        "description": "Test Product Description"
    }
    response = client.post("/product/add", json=data)
    assert response.status_code == 200

def test_list_product(client):
    data = {
        "name": "Test Product Name",
        "description": "Test Product Description"
    }
    client.post("/product/add", json=data)
    response = client.get("/product")
    assert response.status_code == 200


def test_get_specific_product(client):
    data = {
        "name": "Test Product Name",
        "description": "Test Product Description"
    }
    client.post("/product/add", json=data)
    response = client.get("/product/1")
    assert response.status_code == 200


def test_search_keyword(client):
    response = client.get("/product/search?keyword=a")
    assert response.status_code == 200


def test_update_product(client):
    data = {
        "name": "Test Product Name",
        "description": "Test Product Description"
    }
    client.post("/product/add", json=data)
    data = {
        "name": "updated",
        "description": "Test Product Description"
    }
    response = client.put("/product/update/1", json=data)
    assert response.status_code == 200
    assert response.json["name"] == "updated"


def test_delete_product(client):
    data = {
        "name": "Test Product Name",
        "description": "Test Product Description"
    }
    client.post("/product/add", json=data)
    data = {
        "name": "updated",
        "description": "Test Product Description"
    }
    response = client.delete("/product/delete/1", json=data)
    assert response.status_code == 200
