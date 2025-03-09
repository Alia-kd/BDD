from behave import given, when, then
import requests

BASE_URL = "http://localhost:5000"  

@given("the database is initialized with test products")
def step_initialize_database(context):
    """Ensure there are test products in the database"""
    context.products = [
        {"name": "Laptop", "category": "Electronics", "price": 999.99, "stock": 5, "availability": True},
        {"name": "Headphones", "category": "Electronics", "price": 199.99, "stock": 20, "availability": True},
        {"name": "Book", "category": "Books", "price": 19.99, "stock": 50, "availability": True},
    ]
    for product in context.products:
        requests.post(f"{BASE_URL}/products", json=product)

@when('I send a GET request to "{endpoint}"')
def step_get_request(context, endpoint):
    """Send a GET request to the API"""
    context.response = requests.get(f"{BASE_URL}{endpoint}")

@when('I send a PUT request to "{endpoint}" with:')
def step_put_request(context, endpoint):
    """Send a PUT request to update a product"""
    data = {row["field"]: row["value"] for row in context.table}
    context.response = requests.put(f"{BASE_URL}{endpoint}", json=data)

@when('I send a DELETE request to "{endpoint}"')
def step_delete_request(context, endpoint):
    """Send a DELETE request"""
    context.response = requests.delete(f"{BASE_URL}{endpoint}")

@then("the response status code should be {status_code:d}")
def step_check_status_code(context, status_code):
    """Verify the response status code"""
    assert context.response.status_code == status_code, f"Expected {status_code}, got {context.response.status_code}"

@then('the response should contain "{text}"')
def step_check_response_content(context, text):
    """Check if the response contains a specific text"""
    assert text in context.response.text, f"Expected to find {text} in response"

@then("the response should contain a list of products")
def step_check_response_list(context):
    """Check if the response is a list of products"""
    assert isinstance(context.response.json(), list), "Response is not a list"

@then("all returned products should be available")
def step_check_product_availability(context):
    """Ensure all products in response are available"""
    products = context.response.json()
    assert all(product["availability"] for product in products), "Not all products are available"
