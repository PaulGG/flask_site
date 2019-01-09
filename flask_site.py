from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

from app import routes, models
from app import forms
