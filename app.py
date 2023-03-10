# importing flask and the jsonfiy libraries

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'Street Syntax',
     'author': 'Orion Ford',
     'first_sentence': 'Keep Your Vision further than Your Eyesight!',
     'year_published': '2023'},

    {'id': 1,
     'title': 'Dark Roast and Bagels',
     'author': 'StarBuck Chuck',
     'first_sentence': 'I was so hungry, I drank coffee to hold me over while coding.',
     'published': '2015'},

    {'id': 2,
     'title': 'Iphone OR Android...WHAT?!',
     'author': 'Thee Phone Geek',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

# Routing the first method of the home page
@app.route('/', methods=['GET'])
def home():
    return '''<h1>OOO Developer Book Archive</h1>
<p>A prototype API for OOO reads that inspire one to get into the technology space.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()
    return jsonify(books)

'''---- Filtering Code Below --
# This allows each entry within the JSON can be visited
http://127.0.0.1:5000/api/v1/resources/books?id=1

'''


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run()