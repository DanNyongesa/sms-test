# -*-coding:utf-8-*-
"""Configuration file"""
from logging.config import dictConfig


class Config(object):
    """Basic general config"""
    DEBUG = True
    TESTING = False

    @classmethod
    def init_app(cls, app):
        """Class method"""
        # configure logging
        dictConfig({
            'version': 1,
            'formatters': {'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            }},
            'handlers': {'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            }},
            'root': {
                'level': 'INFO',
                'handlers': ['wsgi']
            }
        })


class DevelopmentConfig(Config):
    """Development mode"""
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class ProductionConfig(Config):
    """Development mode"""
    DEBUG = False
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class TestingConfig(Config):
    """Testing config"""
    TESTING = True
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
