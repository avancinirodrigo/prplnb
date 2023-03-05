import os
import sys
path = os.path.dirname(__file__)
sys.path.append(path)
from .api import create_app


app = create_app()