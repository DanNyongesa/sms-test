import os

from app import create_app

config_name = os.environ.get('FLASK_CONFIG') or 'default'
app = create_app(config_name)
