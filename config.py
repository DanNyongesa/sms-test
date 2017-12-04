# -*-coding:utf-8-*-
"""Configuration file"""

from raven.contrib.flask import Sentry
import os

basedir = os.path.abspath(os.path.dirname(__file__))  # base directory


class Config(object):
    """Basic general config"""
    debug = False
    TESTING = False

    # sqlalchemy configs
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # ssl
    SSL_DISABLE = True

    # celery and redis nbackends
    CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
    CELERY_BROKER_URL = os.environ.get('REDIS_URL', "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL', "redis://localhost:6379/0")
    REDIS_URL = os.environ.get('REDIS_URL', "redis://localhost:6379/0")

    # africastalking gateway
    AT_USERNAME = os.environ.get('AT_USERNAME', 'sandbox')
    AT_APIKEY = os.environ.get('AT_APIKEY', 'dbf335184c63c3f7a46af6f399c956d47c7bfd3603610cbaebd1bbe510959d58')
    AT_SHORTCODE = os.environ.get('AT_SHORTCODE', '9999')

    # app admins' email
    ADMINS = ['npiusdan@gmail.com']

    @classmethod
    def init_app(cls, app):
        """Class method"""
        pass


class DevelopmentConfig(Config):
    """Development mode"""
    debug = True
    AT_ENVIRONMENT = 'sandbox'
    CSRF_ENABLED = False
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        import logging
        from logging import getLogger
        from logging.handlers import SysLogHandler

        # log warnings to std input
        sys_handler = SysLogHandler()
        sys_handler.setFormatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
        sys_handler.setLevel(logging.DEBUG)

        # add handlers to loggers
        loggers = [app.logger, getLogger('sqlalchemy')]
        for logger in loggers:
            logger.addHandler(sys_handler)


class ProductionConfig(Config):
    """Development mode"""
    CSRF_ENABLED = True
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        import logging
        from logging import getLogger
        from logging.handlers import SysLogHandler

        # log warnings to std input
        sys_handler = SysLogHandler()
        sys_handler.setFormatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
        sys_handler.setLevel(logging.WARNING)

        # add handlers to loggers
        loggers = [app.logger, getLogger('sqlalchemy')]
        for logger in loggers:
            logger.addHandler(sys_handler)

        sentry = Sentry(dsn='YOUR_DSN_HERE')
        sentry.init_app(app)


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
