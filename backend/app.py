"""
Flask application that acts as an API for Database integration with React application
"""

# Import libraries
import os
import sqlite3
from flask import Flask, send_from_directory, jsonify, g, request
from flask_cors import CORS

# Initialize a Flask application instance, specifying the following:
# - static_folder is set to '../frontend/build' to serve static files from the specified directory (set to '/static' by default),
#   the build directory contains the compiled output of the front-end application. 
# - static_url_path is set to '/' so that static files can be accessed directly from the root URL,
#   eliminating the need for a '/static' prefix.
app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

# Create books.db only in backend directory
DATABASE = os.path.join(os.path.dirname(__file__), 'books.db') 

# Connect to SQLite database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Initialize database
def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        # Books table creation 
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL,
                book_name TEXT NOT NULL,
                author_name TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL
            )
        ''')
        db.commit()

# Automatically close database connection at the end of each request
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Serve React App 
@app.route('/')
@app.route('/<path:path>') 
def serve_react_app(path=''):
    return send_from_directory(app.static_folder, 'index.html')

# API Endpoint for submitting books
@app.route("/api/submit", methods=["POST"])
def submit_book():
    if request.method == "POST":
        data = request.get_json()
        user_name = data["userName"]
        book_name = data["bookName"]
        author_name = data["authorName"]
        category = data["category"]
        description = data["description"]

        db = get_db()
        cursor = db.cursor()

        cursor.execute('''
            INSERT INTO books (user_name, book_name, author_name, category, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_name, book_name, author_name, category, description))
        db.commit()

        return jsonify({"success": True, "message": "Book submitted successfully!"}), 201

# API Endpoint to access records in books table
@app.route("/api/books", methods=["GET"])
def get_books():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()

    # Prepare data in JSON format
    books_data = [
        {
            "id": book[0],
            "user_name": book[1],
            "book_name": book[2],
            "author_name": book[3],
            "category": book[4],
            "description": book[5]
        }
        for book in books
    ]

    return jsonify({"books": books_data})


if __name__ == "__main__":
    init_db()
    CORS(app)
    app.run(debug=True) # Hosted at port 5000 by default.

""" 
# FLASK WEB APPLICATION FOR STATIC FILES (RUN INDEPENDENTLY, NO LINK WITH THE REACT FRONTEND). 
# This makes use of only 'static' and 'Templates' available in the backend directory that are not linked with react frontend 


# A home page (/) that welcomes users and provides a link to the submission form.
# A form page (/form) where users can input their favorite book and author.
# After submitting the form, the application should display a confirmation page (/result) that shows the submitted book and author details.
# Page (/display) checking all the registered books so far stored in the database.

import sqlite3
from flask import Flask, render_template, request, g, jsonify
from flask_cors import CORS

app = Flask(__name__)

DATABASE = 'books.db'

# Connect to database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# Initialise app context 
def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        # Table creation
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL,
                book_name TEXT NOT NULL,
                author_name TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL
            )
        ''')
        db.commit()


# Automatically close database connection at the end of each request
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Home page
@app.route("/", defaults = {"name" : "User"}) # setting default route parameter value for name
@app.route("/<name>") 
def index(name):
    # passing name as a template variable
    return render_template("index.html", username = name)


# Form page
@app.route("/form")
def form():
    return render_template("form.html")


# Result page
@app.route("/result", methods=["POST"])
def result():
    if request.method == "POST":
        # Get data to display
        user_name = request.form["userName"]
        book_name = request.form["bookName"]
        author_name = request.form["authorName"]
        category = request.form["category"]
        description = request.form["description"]

        # Insert data into the database
        db = get_db()
        cursor = db.cursor()
        
        # Parameterized queries
        cursor.execute('''
            INSERT INTO books (user_name, book_name, author_name, category, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_name, book_name, author_name, category, description)) 
        db.commit()

        return render_template("result.html", user_name = user_name, book_name = book_name, author_name = author_name, category = category, description = description)


# Display page - Show all books and authors
@app.route("/display")
def display():
    db = get_db()
    cursor = db.cursor()
    # Fetch all rows from the 'books' table
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    
    return render_template("display.html", books=books)

@app.route("/api/submit", methods=["POST"])
def submit_book():
    if request.method == "POST":
        # Get data from the request
        data = request.get_json()
        user_name = data["userName"]
        book_name = data["bookName"]
        author_name = data["authorName"]
        category = data["category"]
        description = data["description"]

        # Insert data into the database
        db = get_db()
        cursor = db.cursor()

        # Parameterized queries
        cursor.execute('''
            INSERT INTO books (user_name, book_name, author_name, category, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_name, book_name, author_name, category, description))
        db.commit()

        return jsonify({"success": True, "message": "Book submitted successfully!", "data": {
            "userName": user_name,
            "bookName": book_name,
            "authorName": author_name,
            "category": category,
            "description": description
        }}), 201


@app.route("/api/books")
def get_books():
    db = get_db()
    cursor = db.cursor()
    # Fetch all rows from the 'books' table
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    
    # Prepare data in JSON format
    books_data = [
        {
            "id": book[0],
            "user_name": book[1],
            "book_name": book[2],
            "author_name": book[3],
            "category": book[4],
            "description": book[5]
        }
        for book in books
    ]
    
    return jsonify({"books": books_data})


if __name__ == "__main__":
    init_db()
    app.run(debug = True)

"""