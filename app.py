from flask import Flask, jsonify, request
import kagglehub

app = Flask(__name__)


books = [
    {"id":1, "title": "1985", "author": "George Orwell"},
    {"id":2, "title": "Brave New World", "author": "Aldous Huxley"},
]


# Route for get data all books (GET)

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Rout for get a book get by ID (GET)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404


# Append new book (POST)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

# Delete a book (DELETE)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)