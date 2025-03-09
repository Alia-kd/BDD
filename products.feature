Feature: Product Management API
  As a user, I want to manage products via API so that I can retrieve, update, delete, and search for products.

  Scenario: Read a product by ID
    Given the database is initialized with test products
    When I send a GET request to "/products/1"
    Then the response status code should be 200
    And the response should contain "Laptop"

  Scenario: Update a product
    Given the database is initialized with test products
    When I send a PUT request to "/products/1" with:
      | field  | value  |
      | price  | 899.99 |
    Then the response status code should be 200
    And the response should contain "899.99"

  Scenario: Delete a product
    Given the database is initialized with test products
    When I send a DELETE request to "/products/1"
    Then the response status code should be 204
    And the product should no longer exist in the database

  Scenario: List all products
    Given the database is initialized with test products
    When I send a GET request to "/products"
    Then the response status code should be 200
    And the response should contain a list of products

  Scenario: Search by Name
    Given the database is initialized with test products
    When I send a GET request to "/products?name=Laptop"
    Then the response status code should be 200
    And the response should contain "Laptop"

  Scenario: Search by Category
    Given the database is initialized with test products
    When I send a GET request to "/products?category=Electronics"
    Then the response status code should be 200
    And the response should contain "Electronics"

  Scenario: Search by Availability
    Given the database is initialized with test products
    When I send a GET request to "/products?availability=True"
    Then the response status code should be 200
    And all returned products should be available
