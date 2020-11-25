from flask import Flask, render_template, redirect, request, Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("/books", __name__)

# INDEX
# GET '/books'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods=["GET"])
def new_book():
    books = book_repository.select_all()
    return render_template("books/new.html", all_books=books)

# CREATE
# POST '/books'
@books_blueprint.route("/tasks", methods=["POST"])
def create_task():
    # Grab the form data:
    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']
    # Select user using repo:
    author = author_repository.select(author)
    # Create a new book object
    book = Book(title, genre, publisher, author)
    # Save that book object back to the database with the save method
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

