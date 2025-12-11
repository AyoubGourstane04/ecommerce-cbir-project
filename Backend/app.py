from PIL import Image
from flask import Flask, jsonify, request
from flask_cors import CORS
import os

from sqlalchemy import func
from werkzeug.utils import secure_filename

from core.feature_extractor import FeatureExtractor
from core.search_engine import SearchEngine
from database import init_db
from database.models import Product

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:password123@127.0.0.1:5433/ecommerce_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

init_db(app)

fe = FeatureExtractor()
search_engine = SearchEngine("data/features.npy", "data/image_paths.npy")

def sort_product_by_relevance(products, sorted_paths):
    product_map = {p.image_path: p for p in products}
    ordered_products = []

    for path in sorted_paths:
        if path in product_map:
            ordered_products.append(product_map[path])
    return ordered_products


@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.order_by(func.random()).limit(10).all()
    return jsonify([p.to_dict() for p in products]), 200

@app.route('/api/search_image', methods=['POST'])
def search_by_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        img = Image.open(filepath)
        query_vector = fe.extract(img)
        
        raw_paths = search_engine.search(query_vector, top_k=6)
        
        similar_paths = [p.replace('\\', '/') for p in raw_paths]
        
        found_paths = Product.query.filter(Product.image_path.in_(similar_paths)).all()
        
        products = sort_product_by_relevance(found_paths, similar_paths)
        
        return jsonify([p.to_dict() for p in products]), 200
    
    except Exception as e:
        print(f"Error during search: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/search_text', methods=['POST'])
def get_products_by_name():
    product_name = request.form.get('search_value')
    
    if product_name is None or product_name == "":
        return jsonify({"error": "No product selected"}), 400
    
    products = Product.query.filter(Product.name.ilike(f'%{product_name}%')).all()
    
    return jsonify([p.to_dict() for p in products]), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)