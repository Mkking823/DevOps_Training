from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')

with open("configfile.json", "r") as config_file:
    config = json.load(config_file)
    book_api_url = config.get("book_api_url")

# Route to fetch all books from the book management application
@app.route('/booksinfo', methods=['GET'])
def fetch_books():
    response = requests.get(f"{book_api_url}/books")
    if response.status_code == 200:
        books = response.json()
        return jsonify(books)
    else:
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500

# Route to fetch a single book by ID from the book management application
@app.route('/booksinfo/<int:book_id>', methods=['GET'])
def fetch_book(book_id):
    response = requests.get(f"{book_api_url}/books/{book_id}")
    if response.status_code == 200:
        book = response.json()
        return jsonify(book)
    else:
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500

# Route to add a new book to the book management application
@app.route('/booksinfo', methods=['POST'])
def add_book():
    data = request.json
    response = requests.post(f"{book_api_url}/books", json=data)
    if response.status_code == 201:
        return jsonify({"message": "Book added successfully"})
    else:
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500

# Route to update a book by ID in the book management application
@app.route('/booksinfo/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    response = requests.put(f"{book_api_url}/books/{book_id}", json=data)
    if response.status_code == 200:
        return jsonify({"message": "Book updated successfully"})
    else:
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500

# Route to delete a book by ID in the book management application
@app.route('/booksinfo/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    response = requests.delete(f"{book_api_url}/books/{book_id}")
    if response.status_code == 200:
        return jsonify({"message": "Book deleted successfully"})
    else:
        return jsonify({"error": f"Error: {response.status_code} - {response.json()}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
