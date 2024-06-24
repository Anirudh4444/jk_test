from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    with app.app_context():
        from . import routes, auth
        db.create_all()

    return app
