class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+asyncpg://postgres:password@localhost/book_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
    JWT_SECRET_KEY = 'your_jwt_secret_key'
