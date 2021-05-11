import os
# import myEnvVal
# myEnvVal.setVar()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = '97924718a878ea65af465d4656b51eb5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
#db.app = app
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')  
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD') 
mail = Mail(app)

from app import routes