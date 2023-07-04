from flask import Flask
import os

# db = SQLAlchemy()
# DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ['APP_ENCRYPT_KEY']
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}" # where our database is
    # db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app