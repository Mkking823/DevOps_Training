from flask import Flask, request, jsonify
from database import get_books, add_book, get_book, update_book, delete_book
import json
from flask_cors import CORS

def load_config():
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)
        ip_config = config_data.get('IP_CONFIG', {})
        ip = ip_config.get('ip')
        port = ip_config.get('port')
    return config_data, ip, port

app = Flask(__name__)
CORS(app, origins='*')

# Load config and get IP and port
config_data, ip, port = load_config()

# Get all books
@app.route('/books', methods=['GET'])
def get_all_books():
    books = get_books()
    return jsonify(books)

# Get a book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_single_book(book_id):
    book = get_book(book_id)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Add a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    title = data.get('title')
    author = data.get('author')
    year = data.get('year')

    add_book(title, author, year)
    return jsonify({"message": "Book added successfully"}), 201

# Update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_single_book(book_id):
    data = request.json
    title = data.get('title')
    author = data.get('author')
    year = data.get('year')

    update_book(book_id, title, author, year)
    return jsonify({"message": "Book updated successfully"})

# Delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_single_book(book_id):
    delete_book(book_id)
    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    app.run(host=ip, port=port, debug=True)
