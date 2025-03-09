import pytest
from myapp.models import Product

@pytest.fixture
def load_test_data(db):
    """Fixture to populate the database with test data"""
    Product.objects.create(name="Laptop", category="Electronics", price=999.99, stock=5, availability=True)
    Product.objects.create(name="Headphones", category="Electronics", price=199.99, stock=20, availability=True)
    Product.objects.create(name="Book", category="Books", price=19.99, stock=50, availability=True)
