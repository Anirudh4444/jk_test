**Book Management API Documentation**
**Overview**

This API allows for the management of books and reviews in a PostgreSQL database. Users can register, log in, and perform CRUD operations on books and reviews. JWT tokens are used for authentication.
Authentication
All endpoints except /register and /login require a valid JWT token for access.
Endpoints


**User Registration and Login**
Register a New User
•	URL: /register
•	Method: POST
•	Description: Registers a new user.
•	Request Body:


{
  "username": "string",
  "password": "string"
}
•	Response:
o	201 Created: User registered successfully.
o	400 Bad Request: Username already exists.
Log in a User
•	URL: /login
•	Method: POST
•	Description: Logs in a user and returns a JWT token.
•	Request Body:
{
  "username": "string",
  "password": "string"
}
•	Response:
o	200 OK: Returns the JWT token.
o	401 Unauthorized: Invalid username or password.


**Book Management**
Get All Books
•	URL: /books
•	Method: GET
•	Description: Retrieves a list of all books.
•	Response:
o	200 OK: Returns a list of books.
Get a Specific Book
•	URL: /books/<int:book_id>
•	Method: GET
•	Description: Retrieves a specific book by its ID.
•	Response:
o	200 OK: Returns the book details.
o	404 Not Found: Book not found.

Create a New Book
•	URL: /books
•	Method: POST
•	Description: Adds a new book to the database.
•	Request Body:


{
  "title": "string",
  "author": "string",
  "genre": "string",
  "year_published": 2021,
  "summary": "string"
}
•	Response:
o	201 Created: Book added successfully.

Update a Book
•	URL: /books/<int:book_id>
•	Method: PUT
•	Description: Updates the details of an existing book.
•	Request Body:


{
  "title": "string",
  "author": "string",
  "genre": "string",
  "year_published": 2021,
  "summary": "string"
}
•	Response:
o	200 OK: Book updated successfully.
o	404 Not Found: Book not found.
Delete a Book
•	URL: /books/<int:book_id>
•	Method: DELETE
•	Description: Deletes a book from the database.
•	Response:
o	204 No Content: Book deleted successfully.
o	404 Not Found: Book not found.

**Review Management**
Get All Reviews for a Book
•	URL: /books/<int:book_id>/reviews
•	Method: GET
•	Description: Retrieves all reviews for a specific book.
•	Response:
o	200 OK: Returns a list of reviews.
o	404 Not Found: Book not found.
Add a Review to a Book
•	URL: /books/<int:book_id>/reviews
•	Method: POST
•	Description: Adds a review to a specific book.
•	Request Body:


{
  "user_id": 1,
  "review_text": "string",
  "rating": 5
}
•	Response:
o	201 Created: Review added successfully.
o	404 Not Found: Book not found.
Example Requests and Responses
Register a New User
Request:
sh

curl -X POST "http://localhost:5000/register" -H "Content-Type: application/" -d '{
  "username": "newuser",
  "password": "password123"
}'
Response:


{
  "msg": "User registered successfully"
}
Log in a User
Request:
sh

curl -X POST "http://localhost:5000/login" -H "Content-Type: application/" -d '{
  "username": "newuser",
  "password": "password123"
}'
Response:

{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}


**Get All Books**
Request:
sh

curl -X GET "http://localhost:5000/books" -H "Authorization: Bearer <JWT_TOKEN>"
Response:


[
  {
    "id": 1,
    "title": "Test Book",
    "author": "Test Author",
    "genre": "Test Genre",
    "year_published": 2021,
    "summary": "This is a test book summary."
  }
]

Create a New Book
Request:
sh

curl -X POST "http://localhost:5000/books" -H "Authorization: Bearer <JWT_TOKEN>" -H "Content-Type: application/" -d '{
  "title": "New Book",
  "author": "Author Name",
  "genre": "Genre",
  "year_published": 2022,
  "summary": "Summary of the new book"
}'
Response:


{
  "id": 2,
  "title": "New Book",
  "author": "Author Name",
  "genre": "Genre",
  "year_published": 2022,
  "summary": "Summary of the new book"
}

Update a Book
Request:
sh

curl -X PUT "http://localhost:5000/books/2" -H "Authorization: Bearer <JWT_TOKEN>" -H "Content-Type: application/" -d '{
  "title": "Updated Book",
  "author": "Updated Author",
  "genre": "Updated Genre",
  "year_published": 2023,
  "summary": "Updated summary"
}'
Response:


{
  "id": 2,
  "title": "Updated Book",
  "author": "Updated Author",
  "genre": "Updated Genre",
  "year_published": 2023,
  "summary": "Updated summary"
}


Delete a Book
Request:
sh

curl -X DELETE "http://localhost:5000/books/2" -H "Authorization: Bearer <JWT_TOKEN>"
Response:
•	204 No Content
Add a Review to a Book
Request:
sh

curl -X POST "http://localhost:5000/books/1/reviews" -H "Authorization: Bearer <JWT_TOKEN>" -H "Content-Type: application/" -d '{
  "user_id": 1,
  "review_text": "Great book!",
  "rating": 5
}'
Response:


{
  "id": 1,
  "book_id": 1,
  "user_id": 1,
  "review_text": "Great book!",
  "rating": 5
}


****Summary of Endpoints
Endpoint	Method	Description
/register	POST	Register a new user
/login	POST	Log in a user
/books	GET	Get all books
/books	POST	Create a new book
/books/<int:book_id>	GET	Get a specific book by ID
/books/<int:book_id>	PUT	Update a book by ID
/books/<int:book_id>	DELETE	Delete a book by ID
/books/<int:book_id>/reviews	GET	Get all reviews for a specific book
/books/<int:book_id>/reviews	POST	Add a review to a specific book
Description of Test Cases
1.	User Registration and Login
o	Test Case: test_user_registration_and_login
o	Description: Tests the registration and login functionality by creating a new user and verifying login credentials.
2.	Adding a Book
o	Test Case: test_add_book
o	Description: Tests the addition of a new book to the database.
3.	Retrieving All Books
o	Test Case: test_get_books
o	Description: Tests retrieving all books from the database.
4.	Retrieving a Specific Book
o	Test Case: test_get_book
o	Description: Tests retrieving a specific book by its ID.
5.	Updating a Book
o	Test Case: test_update_book
o	Description: Tests updating the details of an existing book.
6.	Deleting a Book
o	Test Case: test_delete_book
o	Description: Tests deleting a book from the database.
7.	Adding a Review
o	Test Case: test_add_review
o	Description: Tests adding a review to a specific book.
8.	Retrieving All Reviews for a Book
o	Test Case: test_get_reviews
o	Description: Tests retrieving all reviews for a specific book.****

