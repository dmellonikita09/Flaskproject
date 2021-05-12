#import os
# import myEnvVal
# myEnvVal.setVar()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message
from app.config import Config
#from flask_admin import Admin
#from app.models import User, Post
#from flask_admin.contrib.sqla import ModelView



db = SQLAlchemy()
#db.app = app
bcrypt = Bcrypt()
#admin = Admin(app)
#admin.add_view(ModelView(User, db.session))
#admin.add_view(ModelView(Post, db.session))
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)



    from app.users.routes import users 
    from app.posts.routes import posts 
    from app.main.routes import main 

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    return app