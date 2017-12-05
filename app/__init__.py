from flask import Flask, render_template
from flask_redis import FlaskRedis
from flask_moment import Moment
from config import CONFIG
from .database import db
from .africastalkinggateway import AT_gateway

redis = FlaskRedis()
moment = Moment()

def create_app(config_name):
    '''Application factory to initialise and configure the application'''
    app = Flask(__name__)
    app.config.from_object(CONFIG[config_name])
    CONFIG[config_name].init_app(app)

    # intialise a database connection instance
    db.init_app(app)

    # intialize redis
    redis.init_app(app)

    # intialize flask moment for formating of datetimes
    moment.init_app(app)

    # intialize Africa's Talking API Gateway wrapper
    AT_gateway.init_app(app)

    # register blueprints
    from .views.main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')
    # register callbacks
    from .views.callbacks import callbacks as callbacks_blueprint
    app.register_blueprint(callbacks_blueprint, url_prefix='/callbacks')
    
    return app