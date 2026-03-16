from flask import Flask, request, jsonify
from flask_cors import CORS

import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

# inicializar flask
app = Flask(__name__)
CORS(app)

load_dotenv()
# conectar con firebase
cred = credentials.Certificate(os.getenv("FIREBASE_KEY_PATH"))
firebase_admin.initialize_app(cred)
db = firestore.client()

# 1 REGISTRAR PRODUCTO

@app.route('/products', methods=['POST'])
def create_product():

    data = request.json
    name = data.get("name")
    stock = data.get("stock")

    if not name or stock is None:
        return jsonify({"error": "Datos incompletos"}), 400

    product = {
        "name": name,
        "stock": stock
    }

    doc_ref = db.collection("products").add(product)

    return jsonify({
        "message": "Producto creado",
        "id": doc_ref[1].id
    }), 201

# 2 CONSULTAR TODOS LOS PRODUCTOS

@app.route('/products', methods=['GET'])
def get_products():

    products = []

    docs = db.collection("products").stream()

    for doc in docs:
        product = doc.to_dict()
        product["id"] = doc.id
        products.append(product)

    return jsonify(products)

# 3 CONSULTAR PRODUCTO POR ID

@app.route('/products/<id>', methods=['GET'])
def get_product(id):

    doc = db.collection("products").document(id).get()

    if not doc.exists:
        return jsonify({"error": "Producto no encontrado"}), 404

    product = doc.to_dict()
    product["id"] = doc.id

    return jsonify(product)

# 4 VERIFICAR STOCK

@app.route('/products/<id>/stock', methods=['GET'])
def check_stock(id):

    doc = db.collection("products").document(id).get()

    if not doc.exists:
        return jsonify({"error": "Producto no encontrado"}), 404

    product = doc.to_dict()

    return jsonify({
        "product_id": id,
        "stock": product["stock"]
    })


# 5 ACTUALIZAR INVENTARIO (VENTA)

@app.route('/products/<id>', methods=['PUT'])
def update_stock(id):

    data = request.json
    quantity = data.get("quantity")

    if quantity is None:
        return jsonify({"error": "Debe enviar quantity"}), 400

    doc_ref = db.collection("products").document(id)
    doc = doc_ref.get()

    if not doc.exists:
        return jsonify({"error": "Producto no encontrado"}), 404

    product = doc.to_dict()

    if product["stock"] < quantity:
        return jsonify({"error": "Stock insuficiente"}), 400

    new_stock = product["stock"] - quantity

    doc_ref.update({
        "stock": new_stock
    })

    return jsonify({
        "message": "Inventario actualizado",
        "stock": new_stock
    })

# INICIAR SERVIDOR

if __name__ == '__main__':
    app.run(port=5000, debug=True)