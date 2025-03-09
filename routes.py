from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from models import Product 
app = Flask(__name__)
api = Api(app)

@api.route('/products/<int:product_id>')
class ProductResource(Resource):
    # 1. Read (Retrieve a product by ID)
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return jsonify(product.to_dict())

    # 2. Update (Modify an existing product)
    def put(self, product_id):
        product = Product.query.get_or_404(product_id)
        data = request.json
        for key, value in data.items():
            setattr(product, key, value)
        product.save()
        return jsonify(product.to_dict())

    # 3. Delete (Remove a product)
    def delete(self, product_id):
        product = Product.query.get_or_404(product_id)
        product.delete()
        return '', 204  # No content response

@api.route('/products')
class ProductListResource(Resource):
    # 4. List All Products
    def get(self):
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products])

    # 5. List by Name
    def get(self):
        name = request.args.get('name')
        category = request.args.get('category')
        availability = request.args.get('availability')

        query = Product.query
        if name:
            query = query.filter(Product.name.ilike(f"%{name}%"))
        if category:
            query = query.filter(Product.category.ilike(f"%{category}%"))
        if availability is not None:
            query = query.filter(Product.availability == (availability.lower() == "true"))

        products = query.all()
        return jsonify([product.to_dict() for product in products])

if __name__ == '__main__':
    app.run(debug=True)
