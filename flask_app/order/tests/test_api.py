
import json
from application import create_app


def test_app_orders(test_app):
    client = test_app.test_client()
    res = client.get('/orders')
    assert res.status_code == 200

def test_app_post_order(test_app):
    client = test_app.test_client()
    data = {
        "description": "New order created from REST API",
        "number_of_pieces": 4,
        "client_id":1
    }
    res = client.post('/order', data=json.dumps(data), headers={"Content-Type": "application/json"},)
    assert res.status_code == 200

def test_app_rand_piece(test_app):
    client = test_app.test_client()
    res = client.post('/rand_piece')
    assert res.status_code == 200

def test_app_get_order(test_app):
    client = test_app.test_client()
    res = client.get('/order/1')
    assert res.status_code == 200

def test_app_delete_order(test_app):
    client = test_app.test_client()
    res = client.delete('/order/1')
    assert res.status_code == 200

def test_app_orders_null(test_app):
    client = test_app.test_client()
    res = client.get('/')
    assert res.status_code == 404

def test_app_delete_order_fail(test_app):
    client = test_app.test_client()
    res = client.delete('/order/-1')
    assert res.status_code == 404

def test_app_get_order_fail(test_app):
    client = test_app.test_client()
    res = client.get('/order/-1')
    assert res.status_code == 404

def test_post_create_order_invalid_json(test_app):
    client = test_app.test_client()
    resp = client.post("/order", data=json.dumps({}), content_type="application/json")
    assert resp.status_code == 400
