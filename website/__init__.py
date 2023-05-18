from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "ldhcp_db.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ldhcp-project'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    from .models import Authentication
     
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return Authentication.query.get(int(id))
    
    return app


def create_database(app:Flask) -> None:
    if not path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created database')
    else:
        print('Database exists')