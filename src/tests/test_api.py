import json
from models import Product
from main import db


def test_healthcheck(client):
    """ Test if healthcheck is reachable"""
    response = client.get('/healthcheck')
    assert response.status_code == 200


def test_get_product_instance(client):
    """ Test if product instance is reachable """
    Product.query.delete()  # implement some proper teardown logic
    name = 'top notch product'
    product = Product(name=name, description='this is new')
    db.session.add(product)
    db.session.commit()

    response = client.get(f'/api/products/{product.slug}')
    api_product = json.loads(response.data)

    assert response.status_code == 200
    assert api_product['name'] == name


def test_create_product_instance(client):
    Product.query.delete()  # implement some proper teardown logic
    name = 'Sheldon Shirt Green Lantern'
    description = '<3 GREEN LANTERN <3'
    category = 'shirts'

    data = {
        'name': name,
        'description': description,
        'category': category
    }

    response = client.post('/api/products', data=json.dumps(data), headers={'Content-type': 'application/json'})
    assert response.status_code == 201
    assert Product.query.filter_by(name=name).first()
