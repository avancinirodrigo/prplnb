from flask import Flask, Blueprint
from webapp.api.database import db
from .config import Config

bp = Blueprint('api', __name__)

def create_app(config=Config):
    app = Flask(__name__)
    db.connect(config.DB_URL)
    db.create_all(overwrite=True)
    app.register_blueprint(bp, url_prefix='/')
    return app

from . import users