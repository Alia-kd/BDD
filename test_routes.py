import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from myapp.models import Product  

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def sample_product(db):
    return Product.objects.create(
        name="Test Product",
        category="Electronics",
        price=99.99,
        stock=10,
        availability=True
    )

# 1. Read Test (Retrieve a product by ID)
def test_read_product(client, sample_product):
    url = reverse('product-detail', args=[sample_product.id])  
    response = client.get(url)
    assert response.status_code == 200
    assert response.json()['name'] == "Test Product"

# 2. Update Test
def test_update_product(client, sample_product):
    url = reverse('product-detail', args=[sample_product.id])
    updated_data = {"price": 79.99}
    response = client.put(url, updated_data, format='json')
    assert response.status_code == 200
    assert response.json()['price'] == 79.99

# 3. Delete Test
def test_delete_product(client, sample_product):
    url = reverse('product-detail', args=[sample_product.id])
    response = client.delete(url)
    assert response.status_code == 204
    assert not Product.objects.filter(id=sample_product.id).exists()

# 4. List All Products
def test_list_all_products(client, db):
    url = reverse('product-list')  # Ensure your route name matches
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# 5. List by Name
def test_list_by_name(client, db):
    Product.objects.create(name="Unique Product", category="Music", price=12.99, stock=3, availability=True)
    url = reverse('product-list') + "?name=Unique Product"
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]['name'] == "Unique Product"

# 6. List by Category
def test_list_by_category(client, db):
    Product.objects.create(name="Gadget", category="Electronics", price=45.99, stock=15, availability=True)
    url = reverse('product-list') + "?category=Electronics"
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.json()) > 0

# 7. List by Availability
def test_list_by_availability(client, db):
    url = reverse('product-list') + "?availability=True"
    response = client.get(url)
    assert response.status_code == 200
    assert all(product["availability"] for product in response.json())
