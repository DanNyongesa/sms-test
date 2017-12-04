# -*-coding:utf-8-*-
"""Configuration file"""

from raven.contrib.flask import Sentry
import os

basedir = os.path.abspath(os.path.dirname(__file__))  # base directory


class Config(object):
    """Basic general config"""
    debug = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ['npiusdan@gmail.com']

    @classmethod
    def init_app(cls, app):
        """Class method"""
        pass


class DevelopmentConfig(Config):
    """Development mode"""

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
    DEBUG = False

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
