from flask import Flask, render_template, redirect, request, Blueprint

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository
from models.book import Book
from models.author import Author

books_blueprint = Blueprint("/books", __name__)

# INDEX
# GET '/books'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/books.html", all_books=books)

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods=["GET"])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors=authors)

# CREATE
# # POST '/books'
@books_blueprint.route("/books", methods=["POST"])
def create_book():
#     # Grab the form data:
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    author_id = request.form['author_id']
#     # Select author using repo:
    author = author_repository.select(author_id)
#     # Create a new book object
    book = Book(title, genre, publisher, author)
#     # Save that book object back to the database with the save method
    book_repository.save(book)
    return redirect('/books')

# SHOW
# GET '/books/<id>'


# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'