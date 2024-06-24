import pytest
from flask import json
from app import create_app, db
from app.models import User, Book, Review

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+asyncpg://user:password@localhost/test_book_management'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def register_user(client, username, password):
    return client.post('/register', data=json.dumps({'username': username, 'password': password}), content_type='application/json')

def login_user(client, username, password):
    return client.post('/login', data=json.dumps({'username': username, 'password': password}), content_type='application/json')

@pytest.mark.asyncio
async def test_user_registration_and_login(client):
    # Test user registration
    response = register_user(client, 'testuser', 'testpassword')
    assert response.status_code == 201
    assert b'User registered successfully' in response.data

    # Test user login
    response = login_user(client, 'testuser', 'testpassword')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'access_token' in data

@pytest.mark.asyncio
async def test_add_book(client):
    # Register and login
    register_user(client, 'testuser', 'testpassword')
    login_response = login_user(client, 'testuser', 'testpassword')
    token = json.loads(login_response.data)['access_token']

    # Add book
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'year_published': 2021,
        'summary': 'This is a test book summary.'
    }
    response = client.post('/books', data=json.dumps(data), headers=headers, content_type='application/json')
    assert response.status_code == 201
    assert b'Test Book' in response.data

@pytest.mark.asyncio
async def test_get_books(client):
    # Register and login
    register_user(client, 'testuser', 'testpassword')
    login_response = login_user(client, 'testuser', 'testpassword')
    token = json.loads(login_response.data)['access_token']

    # Add book for retrieval
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'year_published': 2021,
        'summary': 'This is a test book summary.'
    }
    client.post('/books', data=json.dumps(data), headers=headers, content_type='application/json')

    # Get books
    response = client.get('/books', headers=headers)
    assert response.status_code == 200
    assert b'Test Book' in response.data

@pytest.mark.asyncio
async def test_get_book(client):
    # Register and login
    register_user(client, 'testuser', 'testpassword')
    login_response = login_user(client, 'testuser', 'testpassword')
    token = json.loads(login_response.data)['access_token']

    # Add book for retrieval
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'year_published': 2021,
        'summary': 'This is a test book summary.'
    }
    client.post('/books', data=json.dumps(data), headers=headers, content_type='application/json')

    # Get book by ID
    response = client.get('/books/1', headers=headers)
    assert response.status_code == 200
    assert b'Test Book' in response.data

@pytest.mark.asyncio
async def test_update_book(client):
    # Register and login
    register_user(client, 'testuser', 'testpassword')
    login_response = login_user(client, 'testuser', 'testpassword')
    token = json.loads(login_response.data)['access_token']

    # Add book for update
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'year_published': 2021,
        'summary': 'This is a test book summary.'
    }
    client.post('/books', data=json.dumps(data), headers=headers, content_type='application/json')

    # Update book
    update_data = {
        'title': 'Updated Test Book',
        'author': 'Updated Test Author',
        'genre': 'Updated Test Genre',
        'year_published': 2022,
        'summary': 'This is an updated test book summary.'
    }
    response = client.put('/books/1', data=json.dumps(update_data), headers=headers, content_type='application/json')
    assert response.status_code == 200
    assert b'Updated Test Book' in response.data

@pytest.mark.asyncio
async def test_delete_book(client):
    # Register and login
    register_user(client, 'testuser', 'testpassword')
    login_response = login_user(client, 'testuser', 'testpassword')
    token = json.loads(login_response.data)['access_token']

    # Add book for deletion
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'year_published': 2021,
        'summary': 'This is a test book summary.'
    }
    client.post('/books', data=json.dumps(data), headers=headers, content_type='application/json')

    # Delete book
    response = client.delete('/books/1', headers=headers)
    assert response.status_code == 204
    response = client.get('/books/1', headers=headers)
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_add_review(client):
    # Register and login
    register_user(client, 'testuser', 'testpassword')
    login_response = login_user(client, 'testuser', 'testpassword')
    token = json.loads(login_response.data)['access_token']

    # Add book for review
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'year_published': 2021,
        'summary': 'This is a test book summary.'
    }
    client.post('/books', data=json.dumps(data), headers=headers, content_type='application/json')

    # Add review
    review_data = {
        'user_id': 1,
        'review_text': 'Great book!',
        'rating': 5
    }
    response = client.post('/books/1/reviews', data=json.dumps(review_data), headers=headers, content_type='application/json')
    assert response.status_code == 201
    assert b'Great book!' in response.data

@pytest.mark.asyncio
async def test_get_reviews(client):
    # Register and login
    register_user(client, 'testuser', 'testpassword')
    login_response = login_user(client, 'testuser', 'testpassword')
    token = json.loads(login_response.data)['access_token']

    # Add book for reviews
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        'title': 'Test Book',
        'author': 'Test Author',
        'genre': 'Test Genre',
        'year_published': 2021,
        'summary': 'This is a test book summary.'
    }
    client.post('/books', data=json.dumps(data), headers=headers, content_type='application/json')

    # Add review
    review_data = {
        'user_id': 1,
        'review_text': 'Great book!',
        'rating': 5
    }
    client.post('/books/1/reviews', data=json.dumps(review_data), headers=headers, content_type='application/json')

    # Get reviews
    response = client.get('/books/1/reviews', headers=headers)
    assert response.status_code == 200
    assert b'Great book!' in response.data
