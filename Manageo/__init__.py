from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config
from flask_mail import Mail
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
mail = Mail()
admin = Admin()

def create_app():
    app = Flask(__name__) #init flask
    
    app.config.from_object(Config) #flask config

    db.init_app(app)  
    mail.init_app(app)
    admin.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = "Vous devez être connecté pour voir cette page"
    login_manager.init_app(app)

    

    from .auth import User
    
    @login_manager.user_loader  
    def load_user(user_id):
        return User.query.get(user_id)
    
    
    from .models import  Society, MyModelView, Log

    admin.add_view(MyModelView(Society, db.session))
    admin.add_view(MyModelView(Log, db.session))

    from .auth import auth as auth_blueprint #init auth.py
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint #init main.py
    app.register_blueprint(main_blueprint)

    return app

   

