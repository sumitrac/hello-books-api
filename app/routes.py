from app import db
from flask import Blueprint
from flask import request
from flask import jsonify
from .models.book import Book 

books_bp = Blueprint("books", __name__, url_prefix="/book")
@books_bp.route("/book_id>", methods=["GET"], strict_slashes=False)
def get_single_book(book_id):
    #Try to find the book with the given id 
    book = Book.query.get(book_id)

    if book:
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
        }, 200
    return {
        "message": f"Book with id {book_id} was not found",
        "success": False,
    }, 400


@books.bp.route("", methods=["POST", "GET"], strict_slashes=False)

def books():
    if request.method == "GET":
        books = Book.query.all()
        books_response = {}

        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
                })
        return jsonify(books_response), 200

    else:
        request_body = request.get_json()

        new_book = Book(title = request_body["title"],
                            description=request_body["description"])

        db.session.add(new_book)
        db.session.commit()
        # return (f"book {new_book.title} has been created", 201)
        return {
            "success": True,
            "message": f"Book {new_book.title} has been created"
        }, 201


# hello_world_bp = Blueprint("hello_world", __name__)

# @hello_world_bp.route('/hello-world', methods=["Get"])
# def get_hello_world():
#     my_response = "Hello, World!"
#     return my_response

# @hello_world_bp.route('/hello-world/JSON', methods=["Get"])
# def hello_world_json():
#     return {
#         "name": "Sumi",
#         "message": "Hello",
#         "hobbies": ["Reading", "Coding", "Gardening"],
#     }, 2001


# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body

