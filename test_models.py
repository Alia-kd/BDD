import pytest
from myapp.models import Product  

@pytest.fixture
def sample_product(db):
    return Product.objects.create(
        name="Test Product",
        category="Electronics",
        price=99.99,
        stock=10,
        availability=True
    )

# 1. Read Test
def test_read_product(sample_product):
    product = Product.objects.get(id=sample_product.id)
    assert product.name == "Test Product"

# 2. Update Test
def test_update_product(sample_product):
    sample_product.price = 79.99
    sample_product.save()
    updated_product = Product.objects.get(id=sample_product.id)
    assert updated_product.price == 79.99

# 3. Delete Test
def test_delete_product(sample_product):
    sample_product.delete()
    with pytest.raises(Product.DoesNotExist):
        Product.objects.get(id=sample_product.id)

# 4. List All Products
def test_list_all_products(db):
    Product.objects.create(name="Product 1", category="Books", price=10.99, stock=5, availability=True)
    Product.objects.create(name="Product 2", category="Toys", price=15.99, stock=8, availability=True)
    products = Product.objects.all()
    assert len(products) >= 2  # Ensuring at least two exist

# 5. Find by Name
def test_find_by_name(db):
    Product.objects.create(name="Unique Product", category="Music", price=12.99, stock=3, availability=True)
    product = Product.objects.get(name="Unique Product")
    assert product.category == "Music"

# 6. Find by Category
def test_find_by_category(db):
    Product.objects.create(name="Gadget", category="Electronics", price=45.99, stock=15, availability=True)
    products = Product.objects.filter(category="Electronics")
    assert len(products) > 0

# 7. Find by Availability
def test_find_by_availability(db):
    available_products = Product.objects.filter(availability=True)
    assert available_products.exists()
