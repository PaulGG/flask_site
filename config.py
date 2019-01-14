import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "*4V:-@~Z3zs]T;{KdaZm3U%r=xAQ"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'mail.promisedlan.network'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = ["admin@promisedlan.network"] 
