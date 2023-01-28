## Building RESTAPIs using Python

- app_final.py : is the file from the actual tutorial. the books.db is from the site as well which is read via SQLite.

- new db will be created of the information I have via Postgres.

In this repo the goal is to create APIs using Flask and Python. 

Link: https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#api-terminology



### What are APIs

- connections that send and recv

### How?
	- Flask and Fast API
	- Flask RESTful
	

### API Terminology:
- HTTP
- URL
- JSON
- REST


### API breakdon:
- base URL and the path
- base url: orion3000.xyz
- path: /blog/id/one-day-python-dev


format=json: changes the return data from HTML to JSON.
proxtext=fire: narrows the returned entries to those that include our search term.



### Project: Book catalog
A book catalog API to include data of books title, date of publication and the first sentence of each book. 

Flask will be used for the home page of the the site.

### What does flask do?
Flask maps HTTP requests to Python functions.
Flask provides us with a jsonify function that allows us to convert lists and dictionaries to JSON format.


### Designing Requests (4 Methods defined by the HTTP protocol.)
### using DB https://sqlitebrowser.org/dl/ to view the db fields
CRUD (Create, Read, Update, Delete)

In this repo, I will focus on GET requests, which is reading from a database. Then I will expand it to do all the other methods. (create, update and delete.)

REST API:
GET
POSTS 
PUT 
DELETE

(None of these keywords should beplaced within the request URL.)

- While creating API endpoints, be sure to have them as strong and not weak. Here is an example of the weak endpoint. (Bad Endpoint Ex.)
http://api.example.com/getbook/10

With the endpoint above, it is weak because of the following:
    - get : the keyword is used within the API endpoint itself. thats a nogo. 
    - 10 : obvious that the id is being referred here.


Adding an extra segment on your path such as “resources” or “entries” gives you the option to allow users to search across all resources available, making it easier for you to later support requests such as these: (Good Ex.)
http://api.example.com/resources/books?id=10



### Creating Documentation and Examples
- Without documentation, even the best-designed API will be unusable. Your API should have documentation describing the resources or functionality available through your API that also provides concrete working examples of request URLs or code for your API. 

- A fairly common practice in documenting APIs is to provide annotations in your code that are then automatically collated into documentation using a tool such as Doxygen or Sphinx. 


Great Flask Resource: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
