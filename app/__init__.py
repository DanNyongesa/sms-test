from flask import Flask, render_template
from config import CONFIG


def create_app(config_name):
    '''Application factory to initialise and configure the application'''
    app = Flask(__name__)
    app.config.from_object(CONFIG[config_name])
    CONFIG[config_name].init_app(app)

    # register blueprints
    from . import views as views_blueprint
    app.register_blueprint(views_blueprint, url_prefix='/main')
    return app