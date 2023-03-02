from flask import Flask, Blueprint
from .config import Config

bp = Blueprint('', __name__)

def create_app(config=Config):
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app

from . import routes    