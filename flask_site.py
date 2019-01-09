from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()

from app import routes
